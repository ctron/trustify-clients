use std::{env, error::Error, io, time::Duration};

use reqwest::header::CONTENT_TYPE;
use serde_json::Value;
use trustify_client::TrustifyClient;
use url::{Host, Url};

type ExampleResult<T> = Result<T, Box<dyn Error>>;

pub fn trustify_url() -> String {
    env::var("TRUSTIFY_URL").unwrap_or_else(|_| "http://localhost:8080".to_owned())
}

pub async fn client(base_url: &str) -> ExampleResult<TrustifyClient> {
    let token = access_token().await?;
    let builder = TrustifyClient::builder(base_url);
    let builder = match token {
        Some(token) => builder.bearer_token(token),
        None => builder,
    };
    Ok(builder.build()?)
}

async fn access_token() -> ExampleResult<Option<String>> {
    if let Some(token) = env::var("TRUSTIFY_TOKEN")
        .ok()
        .filter(|token| !token.is_empty())
    {
        if token
            .get(..7)
            .is_some_and(|prefix| prefix.eq_ignore_ascii_case("bearer "))
        {
            return Err(invalid("TRUSTIFY_TOKEN must not include the 'Bearer ' prefix").into());
        }
        return Ok(Some(token));
    }

    let issuer = env::var("ISSUER_URL")
        .ok()
        .filter(|value| !value.is_empty());
    let client_id = env::var("CLIENT_ID").ok().filter(|value| !value.is_empty());
    let client_secret = env::var("CLIENT_SECRET")
        .ok()
        .filter(|value| !value.is_empty());
    if issuer.is_none() && client_id.is_none() && client_secret.is_none() {
        return Ok(None);
    }

    let issuer = issuer.ok_or_else(|| invalid("ISSUER_URL is required for OIDC auth"))?;
    let client_id = client_id.ok_or_else(|| invalid("CLIENT_ID is required for OIDC auth"))?;
    let client_secret =
        client_secret.ok_or_else(|| invalid("CLIENT_SECRET is required for OIDC auth"))?;

    Ok(Some(
        client_credentials_token(&issuer, &client_id, &client_secret).await?,
    ))
}

pub async fn client_credentials_token(
    issuer: &str,
    client_id: &str,
    client_secret: &str,
) -> ExampleResult<String> {
    let issuer_url = validate_url(issuer, "ISSUER_URL", false)?;
    let http = reqwest::Client::builder()
        .timeout(Duration::from_secs(10))
        .redirect(reqwest::redirect::Policy::none())
        .build()?;

    let discovery_url = format!(
        "{}/.well-known/openid-configuration",
        issuer.trim_end_matches('/')
    );
    let metadata: Value = http
        .get(discovery_url)
        .send()
        .await?
        .error_for_status()?
        .json()
        .await?;
    if metadata.get("issuer").and_then(Value::as_str) != Some(issuer) {
        return Err(invalid("OIDC discovery issuer does not match ISSUER_URL").into());
    }
    if let Some(grants) = metadata.get("grant_types_supported") {
        let supports_client_credentials = grants.as_array().is_some_and(|values| {
            values
                .iter()
                .any(|value| value.as_str() == Some("client_credentials"))
        });
        if !supports_client_credentials {
            return Err(invalid("OIDC issuer does not support client_credentials").into());
        }
    }

    let token_endpoint = metadata
        .get("token_endpoint")
        .and_then(Value::as_str)
        .ok_or_else(|| invalid("OIDC discovery is missing token_endpoint"))?;
    let token_url = validate_url(token_endpoint, "token_endpoint", true)?;
    if issuer_url.scheme() == "https" && token_url.scheme() != "https" {
        return Err(invalid("token_endpoint must use HTTPS when ISSUER_URL uses HTTPS").into());
    }

    let auth_methods = metadata.get("token_endpoint_auth_methods_supported");
    let supports_basic = match auth_methods {
        None => true,
        Some(Value::Array(methods)) => methods
            .iter()
            .any(|method| method.as_str() == Some("client_secret_basic")),
        Some(_) => return Err(invalid("OIDC discovery has invalid token auth methods").into()),
    };
    let supports_post = auth_methods
        .and_then(Value::as_array)
        .is_some_and(|methods| {
            methods
                .iter()
                .any(|method| method.as_str() == Some("client_secret_post"))
        });
    if !supports_basic && !supports_post {
        return Err(
            invalid("OIDC issuer must support client_secret_basic or client_secret_post").into(),
        );
    }

    let form = if supports_basic {
        serde_urlencoded::to_string([("grant_type", "client_credentials")])?
    } else {
        serde_urlencoded::to_string([
            ("grant_type", "client_credentials"),
            ("client_id", client_id),
            ("client_secret", client_secret),
        ])?
    };
    let mut request = http
        .post(token_endpoint)
        .header(CONTENT_TYPE, "application/x-www-form-urlencoded")
        .body(form);
    if supports_basic {
        request = request.basic_auth(client_id, Some(client_secret));
    }
    let response = request.send().await?;
    let token: Value = response.error_for_status()?.json().await?;
    let access_token = token
        .get("access_token")
        .and_then(Value::as_str)
        .filter(|value| !value.is_empty())
        .ok_or_else(|| invalid("OIDC token response is missing access_token"))?;
    if token
        .get("token_type")
        .and_then(Value::as_str)
        .is_none_or(|token_type| !token_type.eq_ignore_ascii_case("bearer"))
    {
        return Err(invalid("OIDC token response token_type must be Bearer").into());
    }
    Ok(access_token.to_owned())
}

fn validate_url(raw: &str, name: &str, allow_query: bool) -> ExampleResult<Url> {
    let url = Url::parse(raw)?;
    let loopback = match url.host() {
        Some(Host::Domain(host)) => host.eq_ignore_ascii_case("localhost"),
        Some(Host::Ipv4(address)) => address.is_loopback(),
        Some(Host::Ipv6(address)) => address.is_loopback(),
        None => false,
    };
    if !matches!(url.scheme(), "http" | "https")
        || url.host().is_none()
        || !url.username().is_empty()
        || url.password().is_some()
        || url.fragment().is_some()
        || (!allow_query && url.query().is_some())
    {
        return Err(invalid(format!("{name} must be an absolute HTTP(S) URL")).into());
    }
    if url.scheme() != "https" && !loopback {
        return Err(invalid(format!("{name} must use HTTPS")).into());
    }
    Ok(url)
}

fn invalid(message: impl Into<String>) -> io::Error {
    io::Error::new(io::ErrorKind::InvalidInput, message.into())
}
