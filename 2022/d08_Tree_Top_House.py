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

def part_2(data):
    trees = [[*map(int, line)] for line in data]
    scenic_score = 0

    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[0])-1):
            tree = trees[y][x]
            row = trees[y]
            col = [i[x] for i in trees]

            left = reversed(row[:x])
            right = row[x+1:]
            above = reversed(col[:y])
            below = col[y+1:]

            left_blocked = [i for i,v in enumerate(left) if v-tree >=0]
            left_score= x if len(left_blocked) == 0 else left_blocked[0] + 1

            right_blocked = [i for i,v in enumerate(right) if v-tree >= 0]
            right_score = x if len(right_blocked) == 0 else right_blocked[0]+1

            above_blocked = [i for i,v in enumerate(above) if v-tree >= 0]
            above_score = x if len(above_blocked) == 0 else above_blocked[0]+1

            below_blocked = [i for i,v in enumerate(below) if v-tree >= 0]
            below_score = x if len(below_blocked) == 0 else below_blocked[0]+1

            score = left_score * right_score * above_score * below_score
            if score > scenic_score: scenic_score = score

    return scenic_score


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d08-input.txt')
#data = ["30373","25512","65332","33549","35390"] # test data set
print("Part 1: Consider your map; how many trees are visible from outside the grid?", part_1(data))
print("Part 2: Consider each tree on your map. What is the highest scenic score possible for any tree?", part_2(data))