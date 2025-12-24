#!/usr/bin/env python3
"""
Day 5: Cafeteria

Determine which available ingredient IDs are fresh based on fresh ID ranges.
An ingredient ID is fresh if it falls into any of the given ranges.
"""

def solve():
    # Read the input file
    with open('2025/Day 05: Cafeteria_input.txt', 'r') as f:
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
    
    # Count how many ingredient IDs are fresh (fall into at least one range)
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


if __name__ == '__main__':
    result = solve()
    print(f"Number of fresh ingredient IDs: {result}")

