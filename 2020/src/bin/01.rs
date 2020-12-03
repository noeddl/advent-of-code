use std::path::PathBuf;
use aoc2020::file2vec;

fn get_result1(numbers: &Vec<i32>) -> Option<i32> {
    for n1 in numbers {
        let n2 = 2020 - n1;
        if numbers.contains(&n2) {
            return Some(n1 * n2);
        }
    }

    None
}

fn get_result2(numbers: &Vec<i32>) -> Option<i32> {
    for n1 in numbers {
        for n2 in numbers {
            let n3 = 2020 - n1 - n2;
            if numbers.contains(&n3) {
                return Some(n1 * n2 * n3);
            }
        }
    }

    None
}

fn main() {
    let path = PathBuf::from("inputs/01.txt");
    let strings = file2vec(&path);
    let numbers = strings.iter().map(|n| n.parse().unwrap()).collect();

    let result1 = get_result1(&numbers);
    let result2 = get_result2(&numbers);

    println!("{:?}", result1.unwrap());
    println!("{:?}", result2.unwrap());
}
