# AoC 2022
# --- Day 09 Rope Bridge ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(commands):
    start = [1,1] # (x,y)
    head_x, head_y = 1,1
    tail_x, tail_y = 1,1
    tail_posn_list = []
    delta = {'R': (1,0), 'L': (-1,0), 'U':(0,1), 'D':(0,-1)}
    for line in commands:
        direction = line[0]
        steps = int(line[1])

        for step in range(steps):
            head_x += delta[direction][0]
            head_y += delta[direction][1]
            tail_dist_x = head_x-tail_x
            tail_dist_y = head_y-tail_y
            if abs(tail_dist_x) > 1 or abs(tail_dist_y) > 1: #tail has to move to catch up
                match (tail_dist_x,tail_dist_y):
                    # moves for left right up down first
                    case (2,0):
                        tail_x += 1
                    case (0,2):
                        tail_y += 1
                    case (-2,0):
                        tail_x -= 1
                    case (0,-2):
                        tail_y -= 1
                    # moves for diagonal up right, up left, down left and down right - each has two head positions, but tail move same
                    #up right
                    case (1,2):
                        tail_x += 1
                        tail_y += 1
                    case (2,1):
                        tail_x += 1
                        tail_y += 1
                    # up left
                    case (-1,2):
                        tail_x -= 1
                        tail_y += 1
                    case (-2,1):
                        tail_x -= 1
                        tail_y += 1
                    # down left
                    case (-1,-2):
                        tail_x -= 1
                        tail_y -= 1
                    case (-2,-1):
                        tail_x -= 1
                        tail_y -= 1
                    # down right
                    case (1,-2):
                        tail_x += 1
                        tail_y -= 1
                    case (2,-1):
                        tail_x += 1
                        tail_y -= 1


                if [tail_x,tail_y] not in tail_posn_list: tail_posn_list.append([tail_x,tail_y])
 
    return len(tail_posn_list)+1


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d09-input.txt')
commands = [line.split() for line in input]
# commands = [['R', 4], ['U', 4] , ['L', 3] , ['D', 1], ['R', 4], ['D', 1], ['L', 5], ['R', 2]] # test data
print("Part 1: Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?",part_1(commands))