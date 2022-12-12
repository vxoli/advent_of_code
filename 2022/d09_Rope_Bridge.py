# AoC 2022
# --- Day 09 Rope Bridge ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def move(x,y,direction):
    delta = {'R': (1,0), 'L': (-1,0), 'U':(0,1), 'D':(0,-1), 'UR': (1,1), 'UL': (-1,1), 'DL':(-1,-1), 'DR': (1,-1)}
    new_x = x + delta[direction][0]
    new_y = y + delta[direction][1]
    return [new_x, new_y]

def part_1(commands):
    head_x, head_y = 1,1
    tail_x, tail_y = 1,1
    tail_posn_list = []
    for line in commands:
        direction = line[0]
        steps = int(line[1])

        for step in range(steps):
            head_x, head_y = move(head_x, head_y, direction)
            tail_dist_x = head_x-tail_x
            tail_dist_y = head_y-tail_y
            if abs(tail_dist_x) > 1 or abs(tail_dist_y) > 1: #tail has to move to catch up
                match (tail_dist_x,tail_dist_y):
                    # moves for left right up down first
                    case (2,0):
                        tail_x, tail_y = move(tail_x, tail_y, 'R')
                    case (0,2):
                        tail_x, tail_y = move(tail_x, tail_y, 'U')
                    case (-2,0):
                        tail_x, tail_y = move(tail_x, tail_y, 'L')
                    case (0,-2):
                        tail_x, tail_y = move(tail_x, tail_y, 'D')
                    # moves for diagonal up right, up left, down left and down right - each has two head positions, but tail move same
                    # up right
                    case (1,2) | (2,1):
                        tail_x, tail_y = move(tail_x, tail_y, 'UR')
                    # up left
                    case (-1,2) | (-2,1):
                        tail_x, tail_y = move(tail_x, tail_y, 'UL')
                    # down left
                    case (-1,-2) | (-2,-1):
                        tail_x, tail_y = move(tail_x, tail_y, 'DL')
                    # down right
                    case (1,-2) | (2,-1):
                        tail_x, tail_y = move(tail_x, tail_y, 'DR')

            if [tail_x,tail_y] not in tail_posn_list: tail_posn_list.append([tail_x,tail_y])

    return len(tail_posn_list)

def part_2(commands):
    knots = [[1,1]]*10 # rope consists of ten knots, knots[0] is head, knots[9] is tail knot
    head_x, head_y = knots[0][0], knots[0][1]
    tail_posn_list = []
    for line in commands:
        direction = line[0]
        steps = int(line[1])

        for step in range(steps):
            head_x, head_y = move(head_x, head_y, direction)
            for i, knot in enumerate(knots):
                if i == 0: continue
                tail_x, tail_y = knot
                tail_dist_x = knots[i-1][0]-tail_x
                tail_dist_y = knots[i-1][1]-tail_y
                print(knots)
                print(knot)
                print(tail_dist_x, tail_dist_y)
                if abs(tail_dist_x) > 1 or abs(tail_dist_y) > 1: #tail has to move to catch up
                    match (tail_dist_x,tail_dist_y):
                        # moves for left right up down first
                        case (2,0):
                            tail_x, tail_y = move(tail_x, tail_y, 'R')
                        case (0,2):
                            tail_x, tail_y = move(tail_x, tail_y, 'U')
                        case (-2,0):
                            tail_x, tail_y = move(tail_x, tail_y, 'L')
                        case (0,-2):
                            tail_x, tail_y = move(tail_x, tail_y, 'D')
                        # moves for diagonal up right, up left, down left and down right - each has two head positions, but tail move same
                        # up right
                        case (1,2) | (2,1) | (2,2):
                            tail_x, tail_y = move(tail_x, tail_y, 'UR')
                        # up left
                        case (-1,2) | (-2,1) | (-2,2):
                            tail_x, tail_y = move(tail_x, tail_y, 'UL')
                        # down left
                        case (-1,-2) | (-2,-1) | (-2,-2):
                            tail_x, tail_y = move(tail_x, tail_y, 'DL')
                        # down right
                        case (1,-2) | (2,-1) | (2,-2):
                            tail_x, tail_y = move(tail_x, tail_y, 'DR')
                        case _:
                            print('error')
                            print(knots)
                            print(knot)
                            print(tail_dist_x, tail_dist_y)
                            exit()

                if (knots[:-1] not in tail_posn_list) and ([tail_x, tail_y] not in tail_posn_list): tail_posn_list.append([tail_x,tail_y])

                knots[i] = [tail_x, tail_y]
                knots[0] = [head_x,head_y]

    return len(tail_posn_list)


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d09-input.txt')
commands = [line.split() for line in input]
# commands = [['R', 4], ['U', 4] , ['L', 3] , ['D', 1], ['R', 4], ['D', 1], ['L', 5], ['R', 2]] # test data
#print("Part 1: Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?",part_1(commands))
print(part_2(commands))