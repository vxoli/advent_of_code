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

def max_joltage_12_batteries(bank):
    """Find the maximum joltage by selecting exactly 12 batteries.
    
    We need to pick exactly 12 batteries (digits) maintaining their order.
    The joltage is the number formed by these 12 digits.
    Uses a greedy approach: remove smaller digits from the left when possible.
    """
    digits = [int(d) for d in bank]
    n = len(digits)
    
    if n < 12:
        # If we have fewer than 12 digits, use all of them
        return int(''.join(map(str, digits)))
    
    # We need to remove (n - 12) digits to keep exactly 12
    # Use a stack to build the result greedily
    stack = []
    to_remove = n - 12
    
    for digit in digits:
        # While we can remove digits and current digit is larger than the last in stack
        while stack and to_remove > 0 and digit > stack[-1]:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    # If we still have more than 12 digits, take only the first 12
    # (This can happen if we couldn't remove enough digits)
    if len(stack) > 12:
        stack = stack[:12]
    
    # Convert to integer
    return int(''.join(map(str, stack)))

if __name__ == "__main__":
    input_data = read_data("/home/chris/Documents/code/advent_of_code/2025/Day 03: Lobby.txt")
    
    # Part 1: Select exactly 2 batteries
    total_joltage_part1 = 0
    for bank in input_data:
        max_jolt = max_joltage_for_bank(bank)
        total_joltage_part1 += max_jolt
    
    # Part 2: Select exactly 12 batteries
    total_joltage_part2 = 0
    for bank in input_data:
        max_jolt = max_joltage_12_batteries(bank)
        total_joltage_part2 += max_jolt
    
    print(f"Part 1: {total_joltage_part1}")
    print(f"Part 2: {total_joltage_part2}")
