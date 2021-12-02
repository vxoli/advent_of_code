# Day 01
# --- Report Repair ---
f = "d01p1-input.txt"
data <- as.integer(readLines(f))
part1 <- prod(input[(2020 - input) %in% input])
part2 <- prod(combn(data, 3)[, combn(data, 3, sum) == 2020])
cat("Part 1:", part1, "\n")
cat("Part 2:", part2, "\n")
