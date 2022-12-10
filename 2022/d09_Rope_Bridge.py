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
    headx, heady = 1,1
    tailx, taily = 1,1
    tail_posn_list = []
    delta = {'R': (1,0), 'L': (-1,0), 'U':(0,1), 'D':(0,-1)}
    for line in commands:
        direction = line[0]
        steps = int(line[1])

        for step in range(steps):
            headx += delta[direction][0]
            heady += delta[direction][1]
            tail_dist_x = headx-tailx
            tail_dist_y = heady-taily
            if abs(tail_dist_x) > 1 or abs(tail_dist_y) > 1: #tail has to move to catch up
                match (tail_dist_x,tail_dist_y):
                    # moves for left right up down first
                    case (2,0):
                        tailx += 1
                    case (0,2):
                        taily += 1
                    case (-2,0):
                        tailx -= 1
                    case (0,-2):
                        taily -= 1
                    # moves for diagonal up right, up left, down left and down right - each has two head positions, but tail move same
                    #up right
                    case (1,2):
                        tailx += 1
                        taily += 1
                    case (2,1):
                        tailx += 1
                        taily += 1
                    # up left
                    case (-1,2):
                        tailx -= 1
                        taily += 1
                    case (-2,1):
                        tailx -= 1
                        taily += 1
                    # down left
                    case (-1,-2):
                        tailx -= 1
                        taily -= 1
                    case (-2,-1):
                        tailx -= 1
                        taily -= 1
                    # down right
                    case (1,-2):
                        tailx += 1
                        taily -= 1
                    case (2,-1):
                        tailx += 1
                        taily -= 1

                # # moves for left right up down first
                # if tail_dist_x == 2 and tail_dist_y == 0: #too far right - tail move right to catch up
                #     tailx += 1
                # elif tail_dist_x == 0 and tail_dist_y == 2 : # too far up - tail has to move up                    
                #     taily += 1
                # elif tail_dist_x == -2 and tail_dist_y == 0: # too far left - tail moves left
                #     tailx -= 1
                # elif tail_dist_x == 0 and tail_dist_y == -2: # too far down - tail moves down
                #     taily -= 1
                # # moves for diagonal up right, up left, down left and down right - each has two head positions, but tail move same
                # #up right
                # elif (tail_dist_x == 1 and tail_dist_y == 2) or (tail_dist_x == 2 and tail_dist_y == 1):
                #     tailx += 1
                #     taily += 1
                # # up left
                # elif (tail_dist_x == -1 and tail_dist_y == 2) or (tail_dist_x == -2 and tail_dist_y == 1):
                #     tailx -= 1
                #     taily += 1
                # # down left
                # elif (tail_dist_x == -1 and tail_dist_y == -2) or (tail_dist_x == -2 and tail_dist_y == -1):
                #     tailx -= 1
                #     taily -= 1
                # # down right
                # elif (tail_dist_x == 1 and tail_dist_y == -2) or (tail_dist_x == 2 and tail_dist_y == -1):
                #     tailx += 1
                    # taily -= 1

                if [tailx,taily] not in tail_posn_list: tail_posn_list.append([tailx,taily])
 
    return len(tail_posn_list)+1


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d09-input.txt')
commands = [line.split() for line in input]
#commands = [['R', 4], ['U', 4] , ['L', 3] , ['D', 1], ['R', 4], ['D', 1], ['L', 5], ['R', 2]] # test data
print("Part 1: Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?",part_1(commands))