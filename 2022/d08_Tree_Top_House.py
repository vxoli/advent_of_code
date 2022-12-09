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
    trees = [[*map(int, line)] for line in data]

    vis_trees = 2*(len(trees[0]) + len(trees) -2) # number of trees round the edge

    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[0])-1):
            tree = trees[y][x]
            row = trees[y]
            col = [i[x] for i in trees]

            left = row[:x]
            right = row[x+1:]
            above = col[:y]
            below = col[y+1:]

            if tree > min(max(left), max(right), max(above), max(below)):
                vis_trees += 1

    return vis_trees


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d08-input.txt')
# data = ["30373","25512","65332","33549","35390"]
print(part_1(data))