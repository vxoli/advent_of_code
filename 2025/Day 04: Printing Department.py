#!/usr/bin/env python3
"""
Day 4: Printing Department

Part 1: The forklifts can only access a roll of paper if there are fewer than 
four rolls of paper in the eight adjacent positions.

Part 2: Iteratively remove accessible rolls until no more can be removed.
"""

# Directions for 8 adjacent positions (up, down, left, right, and 4 diagonals)
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),  # top row
    (0, -1),           (0, 1),   # middle row (left, right)
    (1, -1),  (1, 0),  (1, 1)    # bottom row
]


def is_accessible(grid, i, j, rows, cols):
    """Check if a roll at position (i, j) is accessible (has < 4 adjacent rolls)."""
    if grid[i][j] != '@':
        return False
    
    adjacent_rolls = 0
    for di, dj in DIRECTIONS:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == '@':
                adjacent_rolls += 1
    
    return adjacent_rolls < 4


def solve_part1(grid):
    """Part 1: Count how many rolls are initially accessible."""
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    
    accessible_count = 0
    for i in range(rows):
        for j in range(cols):
            if is_accessible(grid, i, j, rows, cols):
                accessible_count += 1
    
    return accessible_count


def solve_part2(grid):
    """Part 2: Iteratively remove accessible rolls until no more can be removed."""
    # Convert grid to list of lists for mutability
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    
    total_removed = 0
    
    # Keep removing accessible rolls until no more can be removed
    while True:
        # Find all accessible rolls in this iteration
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if is_accessible(grid, i, j, rows, cols):
                    to_remove.append((i, j))
        
        # If no rolls can be removed, we're done
        if not to_remove:
            break
        
        # Remove the accessible rolls
        for i, j in to_remove:
            grid[i][j] = '.'
            total_removed += 1
    
    return total_removed


def solve():
    # Read the input file
    with open('2025/Day 04: Printing Department._input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines() if line.strip()]
    
    part1_result = solve_part1(grid)
    part2_result = solve_part2(grid)
    
    return part1_result, part2_result


if __name__ == '__main__':
    part1, part2 = solve()
    print(f"Part 1 - Number of accessible rolls: {part1}")
    print(f"Part 2 - Total rolls that can be removed: {part2}")

