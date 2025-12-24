#!/usr/bin/env python3
"""
Day 5: Cafeteria

Part 1: Determine which available ingredient IDs are fresh based on fresh ID ranges.
Part 2: Count all unique ingredient IDs that are covered by any of the fresh ranges.
"""

def parse_input(filename):
    """Parse the input file and return ranges and ingredient IDs."""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Find the blank line that separates ranges from ingredient IDs
    blank_line_idx = lines.index('')
    
    # Parse ranges (lines before blank line)
    ranges = []
    for line in lines[:blank_line_idx]:
        if line:  # Skip empty lines just in case
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    
    # Parse ingredient IDs (lines after blank line)
    ingredient_ids = []
    for line in lines[blank_line_idx + 1:]:
        if line:  # Skip empty lines
            ingredient_ids.append(int(line))
    
    return ranges, ingredient_ids


def solve_part1(ranges, ingredient_ids):
    """Part 1: Count how many available ingredient IDs are fresh."""
    fresh_count = 0
    
    for ingredient_id in ingredient_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break  # Found in at least one range, no need to check others
        
        if is_fresh:
            fresh_count += 1
    
    return fresh_count


def merge_ranges(ranges):
    """
    Merge overlapping and adjacent ranges.
    Returns a list of non-overlapping merged ranges.
    """
    if not ranges:
        return []
    
    # Sort ranges by start value
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # If current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:
            # Merge: extend the end if necessary
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))
    
    return merged


def solve_part2(ranges):
    """
    Part 2: Count all unique ingredient IDs covered by any of the ranges.
    We merge overlapping ranges and sum up the coverage.
    """
    merged_ranges = merge_ranges(ranges)
    
    total_fresh_ids = 0
    for start, end in merged_ranges:
        # Range is inclusive, so size is (end - start + 1)
        total_fresh_ids += (end - start + 1)
    
    return total_fresh_ids


def solve():
    ranges, ingredient_ids = parse_input('2025/Day 05: Cafeteria_input.txt')
    
    part1_result = solve_part1(ranges, ingredient_ids)
    part2_result = solve_part2(ranges)
    
    return part1_result, part2_result


if __name__ == '__main__':
    part1, part2 = solve()
    print(f"Part 1 - Number of fresh ingredient IDs: {part1}")
    print(f"Part 2 - Total ingredient IDs considered fresh: {part2}")

