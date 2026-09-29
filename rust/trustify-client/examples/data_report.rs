#[path = "common/options.rs"]
mod options;
#[path = "common/mod.rs"]
mod support;

use std::collections::BTreeMap;

use trustify_client::api::{ClientSbomExt, ClientVulnerabilityExt};

fn total_or_unknown(total: Option<i64>) -> String {
    total.map_or_else(|| "unknown".to_owned(), |total| total.to_string())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let Some((limit, _)) = options::parse(100, false)? else {
        return Ok(());
    };
    let base_url = support::trustify_url();
    let client = support::client(&base_url).await?;
    let sboms = client
        .api()
        .list_sboms()
        .sort("ingested:desc")
        .limit(limit)
        .total(true)
        .send()
        .await?
        .into_inner();
    let vulnerabilities = client
        .api()
        .list_vulnerabilities()
        .sort("published:desc")
        .limit(limit)
        .total(true)
        .send()
        .await?
        .into_inner();

    let mut severities = BTreeMap::new();
    for vulnerability in &vulnerabilities.items {
        let severity = vulnerability
            .base_score
            .as_ref()
            .map_or_else(|| "unknown".to_owned(), |score| score.severity.to_string());
        *severities.entry(severity).or_insert(0) += 1;
    }

    println!("Trustify data report: {base_url}");
    println!(
        "SBOMs: {} total; sampled {}",
        total_or_unknown(sboms.total),
        sboms.items.len()
    );
    println!(
        "Vulnerabilities: {} total; sampled {}",
        total_or_unknown(vulnerabilities.total),
        vulnerabilities.items.len()
    );
    println!("Severity in sampled vulnerabilities:");
    for (severity, count) in severities {
        println!("  {severity}: {count}");
    }
    Ok(())
}
