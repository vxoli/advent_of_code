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
    head = [1,1]
    tail = [1,1]
    delta = {'R': (1,0), 'L': (-1,0), 'U':(0,1), 'D':(0,-1)}
    for line in commands:
        direction = line[0]
        steps = int(line[1])

        for step in range(steps):
            head[0] = head[0] + delta[direction][0]
            head[1] = head[1] + delta[direction][1]
            print(head[0], '===', tail[0])
            tail_dist_x = head[0]-tail[0]
            tail_dist_y = head[1]-tail[1]
            print(tail_dist_x, '---', tail_dist_y)
            if tail_dist_x > 1 or tail_dist_y > 1: #tail has to move to catch up
                print('tail move')


    print(head)
    return


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d09-input.txt')
commands = [line.split() for line in input]
commands = [['R', 4], ['U', 4] , ['L', 3] , ['D', 1], ['R', 4], ['D', 1], ['L', 5], ['R', 2]]
print(part_1(commands))