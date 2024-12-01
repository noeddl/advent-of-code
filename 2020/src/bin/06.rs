use std::collections::HashSet;
use std::fs::read_to_string;

fn main() {
    let groups = read_to_string("inputs/06_small.txt").expect("Failed to open file");

    for g in groups
        .split("\n\n")
        .map(|g| g.chars().filter(|&c| c != '\n').collect::<HashSet<_>>())
    {
        println!("{:?} {:?}", g, g.len());
    }

    let sum1: usize = groups
        .split("\n\n")
        .map(|g| {
            g.chars()
                .filter(|&c| c != '\n')
                .collect::<HashSet<_>>()
                .len()
        })
        .sum();

    println!("{:?}", sum1);

    for group in groups.split("\n\n") {
        // let iter = group.lines();

        // let len = iter.next()
        //     .map(|l| l.chars().collect::<HashSet<_>>())
        //     .map(|line| iter.fold(line, |l1, l2| l1.intersection(&l2)).len());

        // println!("{:?}", len);
        // for line in group.lines() {
        //    let iter = line.chars().collect::<HashSet<_>>();
        // }

        let sets: Vec<_> = group.lines().map(|l| l.chars().collect::<HashSet<_>>()).collect();

        println!("{:?}", sets);

        let iter = sets.iter();
        let len = iter.next().map(|set| iter.fold(set, |set1, set2| &(set1 & set2)));

        println!("{:?}", len);
    }

    // let sum2: usize = groups
    //     .split("\n\n")
    //     .map(|g| {
    //         g.lines()
    //             .map(|l| l.chars().collect::<HashSet<_>>())
    //             .map(|l| fold(set, |set1, set2| set1 & set2)
    //             //.fold(HashSet::new(), |acc, x| {
    //             //    acc.intersection(x).collect()
    //             //})
    //             .len()
    //     })
    //     .sum();

    //println!("{:?}", sum2);
}
