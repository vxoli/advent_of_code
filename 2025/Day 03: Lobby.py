def read_data(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

def max_joltage_for_bank(bank):
    """Find the maximum two-digit joltage from a bank of batteries."""
    digits = [int(d) for d in bank]
    n = len(digits)
    
    if n < 2:
        return 0
    
    max_joltage = 0
    
    # For each position i (as tens digit), find the max digit after it (as ones digit)
    for i in range(n - 1):
        # Find the maximum digit that appears after position i
        max_ones = max(digits[i + 1:])
        joltage = digits[i] * 10 + max_ones
        max_joltage = max(max_joltage, joltage)
    
    return max_joltage

if __name__ == "__main__":
    input_data = read_data("/home/chris/Documents/code/advent_of_code/2025/Day 03: Lobby.txt")
    
    total_joltage = 0
    for bank in input_data:
        max_jolt = max_joltage_for_bank(bank)
        total_joltage += max_jolt
    
    print(f"Total output joltage: {total_joltage}")
