def read_data(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

def max_joltage_for_bank(bank):
    """Find the maximum two-digit joltage from a bank of batteries.
    
    We need to pick exactly two batteries (digits) where the first appears
    before the second in the string. The joltage is the two-digit number
    formed by these digits in order.
    """
    digits = [int(d) for d in bank]
    n = len(digits)
    
    if n < 2:
        return 0
    
    max_joltage = 0
    
    # Try all possible pairs: first battery at position i, second at position j > i
    for i in range(n):
        for j in range(i + 1, n):
            joltage = digits[i] * 10 + digits[j]
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

if __name__ == "__main__":
    input_data = read_data("/home/chris/Documents/code/advent_of_code/2025/Day 03: Lobby.txt")
    
    total_joltage = 0
    for bank in input_data:
        max_jolt = max_joltage_for_bank(bank)
        total_joltage += max_jolt
    
    print(f"Total output joltage: {total_joltage}")
