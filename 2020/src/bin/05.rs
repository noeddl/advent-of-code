use aoc2020::file2vec;

fn decode(codes: &[char], min: u8, max: u8) -> (&[char], u8, u8) {
    if codes.is_empty() {
        return (codes, min, max);
    }

    let code = codes[0];
    let new_codes = &codes[1..];

    let half_len = (max + 1 - min) / 2;
    let middle = min + half_len;

    if code == 'F' || code == 'L' {
        //println!("{:?} {:?} {:?}", &new_codes, min, middle - 1);
        return decode(&new_codes, min, middle - 1);
    }

    //println!("{:?} {:?} {:?}", &new_codes, middle, max);
    decode(&new_codes, middle, max)
}

fn get_seat(codes: &[char]) -> (u8, u8) {
    let (_, row, _) = decode(&codes[..7], 0, 127);
    let (_, col, _) = decode(&codes[7..], 0, 7);

    (row, col)
}

fn main() {
    let strings = file2vec("inputs/05.txt");

    let ids: Vec<_> = strings
        .iter()
        .map(|s| s.chars().collect::<Vec<_>>())
        .map(|codes| get_seat(&codes))
        .map(|(row, col)| row as u16 * 8 + col as u16)
        .collect();

    // Part 1: Get the highest id in the list.
    let max_id = ids.iter().max().unwrap();
    println!("{:?}", max_id);

    // Part 2: Get the missing id.
    let min_id = ids.iter().min().unwrap();

    for id in *min_id..*max_id {
        if !ids.contains(&id) {
            println!("{:?}", id);
        }
    }
}
