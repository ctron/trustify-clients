#[path = "common/options.rs"]
mod options;
#[path = "common/mod.rs"]
mod support;

use trustify_client::api::ClientSbomExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let Some((limit, query)) = options::parse(20, true)? else {
        return Ok(());
    };
    let base_url = support::trustify_url();
    let client = support::client(&base_url).await?;
    let mut request = client
        .api()
        .list_sboms()
        .sort("ingested:desc")
        .limit(limit)
        .total(true);
    if let Some(query) = query {
        request = request.q(query);
    }
    let page = request.send().await?.into_inner();

    println!(
        "SBOMs on {base_url}: {} total; showing {}",
        page.total
            .map_or_else(|| "unknown".to_owned(), |total| total.to_string()),
        page.items.len()
    );
    for sbom in page.items {
        println!(
            "{:?}  {:>7} packages  {}  [{}]",
            sbom.ingested, sbom.number_of_packages, sbom.name, sbom.id
        );
    }
    Ok(())
}
