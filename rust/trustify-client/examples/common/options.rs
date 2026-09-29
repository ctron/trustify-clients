use std::{error::Error, io};

pub type Parsed = (i64, Option<String>);

pub fn parse(default_limit: i64, allow_query: bool) -> Result<Option<Parsed>, Box<dyn Error>> {
    let mut args = std::env::args();
    let program = args.next().unwrap_or_else(|| "example".to_owned());
    let mut limit = default_limit;
    let mut query = None;

    while let Some(argument) = args.next() {
        match argument.as_str() {
            "--limit" => {
                limit = args
                    .next()
                    .ok_or_else(|| invalid("--limit requires a value"))?
                    .parse()?;
            }
            "--query" if allow_query => {
                query = Some(
                    args.next()
                        .ok_or_else(|| invalid("--query requires a value"))?,
                );
            }
            "-h" | "--help" => {
                let query_option = if allow_query { " [--query QUERY]" } else { "" };
                println!("Usage: {program} [--limit N]{query_option}");
                return Ok(None);
            }
            _ => return Err(invalid(format!("unknown argument: {argument}")).into()),
        }
    }

    if limit < 1 {
        return Err(invalid("--limit must be greater than zero").into());
    }
    Ok(Some((limit, query)))
}

fn invalid(message: impl Into<String>) -> io::Error {
    io::Error::new(io::ErrorKind::InvalidInput, message.into())
}
