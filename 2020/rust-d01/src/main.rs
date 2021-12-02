use std::str::FromStr;

fn main() {
    let input = read_all_as::<u32>("/home/christopher/Documents/GitHub/adventofcode2020/d01p1-input.txt");
    let mut answer = part1(&input);
    println!("Part 1: product = {}", answer);
    answer = part2(&input);
    println!("Part 2: product = {}", answer);
}

fn part1(expenses: &[u32]) -> u32 {
    for (pos1, expense1) in expenses.iter().enumerate() {
        for (pos2, expense2) in expenses.iter().enumerate() {
            if pos1 != pos2 && expense1 + expense2 == 2020 {
                return expense1 * expense2;
            }
        }
    }
    panic!("Couldn't find 2 expenses that add up to 2020")
}

fn part2(expenses: &[u32]) -> u32 {
    for (pos1, expense1) in expenses.iter().enumerate() {
        for (pos2, expense2) in expenses.iter().enumerate() {
            for (pos3, expense3) in expenses.iter().enumerate() {
                if pos1 != pos2 && pos2 != pos3 && expense1 + expense2 + expense3 == 2020 {
                    return expense1 * expense2 * expense3;
                }
            }
        }
    }
    panic!("Couldn't find 3 expenses that add up to 2020")
}

fn read_all_as<T: FromStr>(file_name: &str) -> Vec<T> {
    read_all(file_name)
        .iter()
        .map(|x| match x.parse::<T>() {
            Ok(n) => n,
            Err(_) => panic!("Failed to parse"),
        })
        .collect()
}

fn read_all(file_name: &str) -> Vec<String> {
    std::fs::read_to_string(file_name)
        .expect("file not found!")
        .lines()
        .map(|line| line.to_string())
        .collect()
}
