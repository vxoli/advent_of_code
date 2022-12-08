# AoC 2022
# --- Day 08 Tree Top House ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data
def part_1(grid):

    vis_grid = [['T' for y in range(len(grid[0]))] for x in range(len(grid))]
    for row, line in enumerate(grid):
        for col, tree in enumerate(line):
            if row -1 <0 or col -1 < 0 or row == len(grid)-1 or col == len(grid[0])-1: #tree is on the edge and so is visable
                vis_grid[row][col]='V'
                continue
            # if  grid[row][col]> grid[row-1][col] and vis_grid[row-1][col]=='V': # visable from left
            #     vis_grid[row][col]='V'
            # if grid[row][col] > grid[row][col-1] and vis_grid[row][col-1]=='V': #visable from above
            #     vis_grid[row][col]='V'
            # if grid[row][col] > grid[row+1][col] and vis_grid[row+1][col] == 'V': #visable from right
            #     vis_grid[row][col]='V'
            # if grid[row][col] > grid[row][col+1] and vis_grid[row][col+1] == 'V': #visable from right
            #     vis_grid[row][col]='V'        

    total = 0
    for row in vis_grid:
        print(row)
        total += row.count('V')

    return total


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d08-input.txt')
test_data = ["30373","25512","65332","33549","35390"]
print(part_1(test_data))