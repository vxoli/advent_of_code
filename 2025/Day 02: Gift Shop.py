def is_invalid_id_part1(num):
    """
    Part 1: Check if a number is invalid (made of a sequence of digits repeated exactly twice).
    Examples: 55, 6464, 123123
    """
    s = str(num)
    length = len(s)
    
    # Must have even length to be split in half
    if length % 2 != 0:
        return False
    
    # Split in half and check if both halves are identical
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]
    
    return first_half == second_half


def is_invalid_id_part2(num):
    """
    Part 2: Check if a number is invalid (made of a sequence of digits repeated at least twice).
    Examples: 55, 6464, 123123, 12341234, 123123123, 1212121212, 1111111
    """
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    # (we need at least 2 repetitions, so pattern can't be longer than half)
    for pattern_len in range(1, length // 2 + 1):
        # The total length must be divisible by pattern length
        if length % pattern_len != 0:
            continue
        
        # Extract the pattern
        pattern = s[:pattern_len]
        
        # Check if the entire string is composed of this pattern repeated
        num_repetitions = length // pattern_len
        if num_repetitions >= 2:  # At least 2 repetitions required
            reconstructed = pattern * num_repetitions
            if reconstructed == s:
                return True
    
    return False


def parse_ranges(input_file):
    """Parse the input file and return a list of (start, end) tuples."""
    with open(input_file, 'r') as f:
        line = f.read().strip()
    
    ranges = []
    for range_str in line.split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    return ranges


def solve_part(validator_func, ranges):
    """Find all invalid IDs using the given validator function."""
    invalid_ids = []
    for start, end in ranges:
        for num in range(start, end + 1):
            if validator_func(num):
                invalid_ids.append(num)
    
    return sum(invalid_ids)


def solve():
    # Read and parse input
    input_file = '/home/chris/Documents/code/advent_of_code/2025/Day 02: Gift Shop.txt'
    ranges = parse_ranges(input_file)
    
    # Solve Part 1
    part1_total = solve_part(is_invalid_id_part1, ranges)
    print(f"Part 1: {part1_total}")
    
    # Solve Part 2
    part2_total = solve_part(is_invalid_id_part2, ranges)
    print(f"Part 2: {part2_total}")
    
    return part1_total, part2_total


if __name__ == '__main__':
    solve()