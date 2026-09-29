#[path = "common/mod.rs"]
mod support;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let base_url = support::trustify_url();
    let client = support::client(&base_url).await?;

    let info = client.api().info().send().await?;
    let info = info.into_inner();
    println!("Server: {base_url}");
    println!("Version: {}", info.version);
    println!("Read only: {}", info.read_only);
    println!("Exploit intelligence: {}", info.exploit_intelligence);
    Ok(())
}
