use std::{
    io::{BufRead, BufReader, Read, Write},
    net::TcpListener,
    thread,
};

#[allow(dead_code)]
#[path = "../examples/common/mod.rs"]
mod support;

#[tokio::test]
async fn exchanges_oidc_client_credentials_for_a_bearer_token() {
    let listener = TcpListener::bind("127.0.0.1:0").unwrap();
    let issuer = format!("http://{}", listener.local_addr().unwrap());
    let server_issuer = issuer.clone();
    let server = thread::spawn(move || {
        for _ in 0..2 {
            let (stream, _) = listener.accept().unwrap();
            let mut stream = BufReader::new(stream);
            let mut request_line = String::new();
            stream.read_line(&mut request_line).unwrap();
            let path = request_line.split_whitespace().nth(1).unwrap().to_owned();

            let mut headers = std::collections::HashMap::new();
            let mut line = String::new();
            loop {
                line.clear();
                stream.read_line(&mut line).unwrap();
                if line == "\r\n" {
                    break;
                }
                let (name, value) = line.split_once(':').unwrap();
                headers.insert(name.to_ascii_lowercase(), value.trim().to_owned());
            }
            let length = headers
                .get("content-length")
                .map_or(0, |length| length.parse().unwrap());
            let mut body = vec![0; length];
            stream.read_exact(&mut body).unwrap();

            let response_body = if path == "/.well-known/openid-configuration" {
                serde_json::json!({
                    "issuer": server_issuer,
                    "token_endpoint": format!("{server_issuer}/token"),
                    "grant_types_supported": ["client_credentials"],
                    "token_endpoint_auth_methods_supported": ["client_secret_basic"]
                })
                .to_string()
            } else {
                assert_eq!(path, "/token");
                assert_eq!(
                    headers.get("authorization").map(String::as_str),
                    Some("Basic Y2xpZW50OnNlY3JldA==")
                );
                assert_eq!(body, b"grant_type=client_credentials");
                r#"{"access_token":"example-token","token_type":"Bearer"}"#.to_owned()
            };
            let mut stream = stream.into_inner();
            write!(
                stream,
                "HTTP/1.1 200 OK\r\ncontent-type: application/json\r\ncontent-length: {}\r\nconnection: close\r\n\r\n{}",
                response_body.len(),
                response_body
            )
            .unwrap();
        }
    });

    let token = support::client_credentials_token(&issuer, "client", "secret")
        .await
        .unwrap();
    server.join().unwrap();
    assert_eq!(token, "example-token");
}
