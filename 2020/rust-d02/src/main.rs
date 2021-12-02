/* # Day 2: 
## --- Password Philosophy ---
## --- Part One ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

- 1-3 a: abcde
- 1-3 b: cdefg
- 2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

To begin, get your puzzle input. 

## --- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

- 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
- 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
- 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
*/

use std::fs;

fn main() {
    let filename = "/home/christopher/Documents/GitHub/adventofcode2020/d02-input.txt";
    let data = read_input_data(filename);
    let mut validpart1: i32 = 0;
    let mut validpart2: i32 = 0;
    for (_index, line) in data.iter().enumerate() {
        // split the string into min, max, letter and pasword
        let (min, max, letter, password) = split_the_line(line);
        // Part 1: check if count falls into the rage allowed
        if count_part1(letter, password, min, max) {validpart1 += 1; }
        // Part 2 check if one and only one of the positions in password contains the letter
        if count_part2(letter, password, min, max) {validpart2 += 1;}
    }
    println!("Part 1: valid passwords = {}", validpart1);
    println!("Part 2: valid passwords = {}", validpart2);
} // End of main function

//Start function definitions

fn read_input_data(filename: &str) -> Vec<String> {
    let input = fs::read_to_string(filename)
                    .unwrap()
                    .lines()
                    .map(|line| line.to_string())
                    .collect();
    input
}

fn split_the_line(line: &str) -> (i32, i32, char, &str) {
    let split_string = line.split(" ").collect::<Vec<&str>>();
    let min: i32 = split_string[0].split("-").collect::<Vec<&str>>()[0].parse::<i32>().unwrap();
    let max: i32 = split_string[0].split("-").collect::<Vec<&str>>()[1].parse::<i32>().unwrap();
    let letter: char = split_string[1].split(":").collect::<Vec<&str>>()[0].parse::<char>().unwrap();
    (min, max, letter, split_string[2])
}

fn count_part1(letter: char, password: &str, min:i32, max: i32) -> bool {
            // clumsy for loop to count occurrences of the letter in password
            let mut occurrences: i32 = 0;
            let mut valid: bool = false;
            for c in password.chars() {
                if c == letter {
                    occurrences += 1;
                }
            }
            if occurrences <= max && occurrences >= min {valid = !valid;}
            valid
}

fn count_part2(letter: char, password: &str, min: i32, max: i32) -> bool {
    let mut valid: bool = false;
    for (index, ch) in password.chars().enumerate() {
        if ((index + 1) as i32 == min || (index+1) as i32 == max )&& ch == letter {valid = !valid;}
    }
    valid
}