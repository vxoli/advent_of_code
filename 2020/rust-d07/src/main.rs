/* # Day 7:
## --- Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

- light red bags contain 1 bright white bag, 2 muted yellow bags.
- dark orange bags contain 3 bright white bags, 4 muted yellow bags.
- bright white bags contain 1 shiny gold bag.
- muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
- shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
- dark olive bags contain 3 faded blue bags, 4 dotted black bags.
- vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
- faded blue bags contain no other bags.
- dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

- A bright white bag, which can hold your shiny gold bag directly.
- A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
- A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
- A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
- So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

*/
use std::fs;

fn main() {
    let data = read_input_data("../d07-input.txt");
    // split data into bag and what it contains
    //let mut my_bags= Vec::new();
    let mut bags = Vec::<&str>::new();
    //find bags that can contain "shiny gold" bags
    for line in data.iter() {
        let splitline: Vec<&str> = line.split(" contain ").collect();
        if splitline[1].contains("shiny gold") {
            bags.push(
                splitline[0]
                    .trim_end_matches("s")
                    .trim_end_matches("bag")
                    .trim(),
            );
        }
    }
    //now find the bags that can contain bags that can contain "shiny gold" bags
    // I think I need a while loop to loop over the possibile bag colours, identify more_bags,
    // update bags with more_bags and repeat till no further bags found.
    // need to exclude bags already found
    // if more_bags.iter().any()(|&bag| bag == bag_col) {skip pushing onto vector}
    let mut more_bags = Vec::<&str>::new();
    let mut num_new_bags = bags.len();
    while num_new_bags != 0 {
        for bag_col in bags.iter() {
            for line in data.iter() {
                let splitline: Vec<&str> = line.split(" contain ").collect();
                if splitline[1].contains(bag_col) && !bags.contains(&splitline[1]) {
                    more_bags.push(
                        splitline[0]
                            .trim_end_matches("s")
                            .trim_end_matches("bag")
                            .trim(),
                    );
                }
            }
        }
        num_new_bags = more_bags.len();

        bags.append(&mut more_bags);
        println!("{:?} - {}", more_bags, more_bags.len());
        println!("{:?} - {}", bags.len(), num_new_bags);
    }
}

fn read_input_data(filename: &str) -> Vec<String> {
    let input = fs::read_to_string(filename)
        .unwrap()
        .lines()
        .map(|line| line.to_string())
        .collect();
    input
}
