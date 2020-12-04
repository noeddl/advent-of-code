use regex::Regex;
use std::collections::HashMap;
use std::fs::read_to_string;

fn has_all_fields(passport: &str) -> bool {
    let codes = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

    for code in codes {
        if !passport.contains(code) {
            return false;
        }
    }

    true
}

fn is_valid_year(value: &str, min: u16, max: u16) -> bool {
    if value.len() != 4 {
        return false;
    }

    let val = value.parse().unwrap();

    if min <= val && val <= max {
        return true;
    }

    false
}

fn is_valid_hgt(value: &str) -> bool {
    let num: u16 = value[..value.len() - 2].parse().unwrap();

    if value.ends_with("cm") && 150 <= num && num <= 193 {
        return true;
    }

    if value.ends_with("in") && 59 <= num && num <= 76 {
        return true;
    }

    false
}

fn is_valid_hcl(value: &str) -> bool {
    let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();

    re.is_match(&value)
}

fn is_valid_ecl(value: &str) -> bool {
    let colors = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];

    colors.contains(&value)
}

fn is_valid_pid(value: &str) -> bool {
    let re = Regex::new(r"^[0-9]{9}$").unwrap();

    re.is_match(&value)
}

fn is_valid(entries: &HashMap<&str, &str>) -> bool {
    let byr = entries.get("byr").unwrap();
    let iyr = entries.get("iyr").unwrap();
    let eyr = entries.get("eyr").unwrap();
    let hgt = entries.get("hgt").unwrap();
    let hcl = entries.get("hcl").unwrap();
    let ecl = entries.get("ecl").unwrap();
    let pid = entries.get("pid").unwrap();

    is_valid_year(&byr, 1920, 2002)
        && is_valid_year(&iyr, 2010, 2020)
        && is_valid_year(&eyr, 2020, 2030)
        && is_valid_hgt(&hgt)
        && is_valid_hcl(&hcl)
        && is_valid_ecl(&ecl)
        && is_valid_pid(&pid)
}

fn count_valid1(passports: &str) -> u8 {
    let mut count = 0;

    for passport in passports.split("\n\n") {
        if has_all_fields(&passport) {
            count += 1;
        }
    }

    count
}

fn count_valid2(passports: &str) -> u8 {
    let mut count = 0;

    for passport in passports.split("\n\n") {
        if !has_all_fields(&passport) {
            continue;
        }

        let fields: Vec<_> = passport.trim().split(|c| c == ' ' || c == '\n').collect();
        let mut entries = HashMap::new();

        for field in fields {
            let k_v: Vec<_> = field.split(':').collect();
            entries.insert(k_v[0], k_v[1]);
        }

        if is_valid(&entries) {
            count += 1;
        }
    }

    count
}

fn main() {
    let passports = read_to_string("inputs/04.txt").expect("Failed to open file");

    let count1 = count_valid1(&passports);
    let count2 = count_valid2(&passports);

    println!("{:?}", count1);
    println!("{:?}", count2);
}
