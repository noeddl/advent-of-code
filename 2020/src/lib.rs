use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::path::PathBuf;

pub fn file2vec(path_str: &str) -> Vec<String> {
    let path = PathBuf::from(path_str);
    let f = File::open(path).expect("Failed to open file");
    BufReader::new(f)
        .lines()
        .map(|line| line.unwrap())
        .collect()
}
