#AoC 2022
# --- Day 05: Supply Stacks ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
    # cleanup data set into sections: starting crate positions and the moves
    #moves can be broken down into number crates and from and to locations
    # use stack datastructures for each stack crates to track whats been added and moved.
    linecount = 0
    stacks_start = []
    for line in data:
        if line == '': break
        linecount += 1
        stacks_start.append(line)
    stack_1, stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9 = [],[],[],[],[],[],[],[],[]
    # loop through stacks_start in reverse order to add crates to stacks, and skip bottom row of numbers

    for i in range(linecount-2, -1, -1):
        # split line by groups of 4 chars
        if stacks_start[i][0:3].strip('[').strip(' ').strip(']') != '':
            stack_1.append(stacks_start[i][0:3].strip('[').strip(' ').strip(']'))
        if stacks_start[i][4:7].strip('[').strip(' ').strip(']'):
            stack_2.append(stacks_start[i][4:7].strip('[').strip(' ').strip(']'))
        if stacks_start[i][8:11].strip('[').strip(' ').strip(']'):
            stack_3.append(stacks_start[i][8:11].strip('[').strip(' ').strip(']'))
        if stacks_start[i][12:15].strip('[').strip(' ').strip(']') != '':
            stack_4.append(stacks_start[i][12:15].strip('[').strip(' ').strip(']'))
        if stacks_start[i][16:19].strip('[').strip(' ').strip(']') != '':
            stack_5.append(stacks_start[i][16:19].strip('[').strip(' ').strip(']'))
        if stacks_start[i][20:24].strip('[').strip(' ').strip(']') != '':
            stack_6.append(stacks_start[i][20:24].strip('[').strip(' ').strip(']'))
        if stacks_start[i][25:28].strip('[').strip(' ').strip(']') != '':
            stack_7.append(stacks_start[i][25:28].strip('[').strip(' ').strip(']'))
        if stacks_start[i][29:32].strip('[').strip(' ').strip(']') != '':
            stack_8.append(stacks_start[i][29:32].strip('[').strip(' ').strip(']'))
        if stacks_start[i][33:36].strip('[').strip(' ').strip(']') != '':
            stack_9.append(stacks_start[i][33:36].strip('[').strip(' ').strip(']'))

    # put stacks into a dictionary - tried to combine this with step above but got confused.
    stack = {}
    stack[1], stack[2], stack[3], stack[4], stack[5], stack[6], stack[7], stack[8], stack[9] = stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9
    # now clean instructions into number of crates to move and from and to stacks
    for line in data:
        if 'move' in line:
            num_to_move = int(line.split(' ')[1])
            move_from = int(line.split(' ')[3])
            move_to = int(line.split(' ')[5])

            for i in range(num_to_move):
                stack[move_to].append(stack[move_from].pop())

    #which crates are at the top of each stack
    top_crates = []
    for i in range(1,10):
        top_crates.append(stack[i].pop())

    return top_crates

def part_2(data):
    # cleanup data set into sections: starting crate positions and the moves
    #moves can be broken down into number crates and from and to locations
    # use stack datastructures for each stack crates to track whats been added and moved.

    # I SHOULD USED FUNCTIONS HERE THAT CAN BE CALLED FROM PART_1 AND PART_2

    linecount = 0
    stacks_start = []
    for line in data:
        if line == '': break
        linecount += 1
        stacks_start.append(line)
    stack_1, stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9 = [],[],[],[],[],[],[],[],[]
    # loop through stacks_start in reverse order to add crates to stacks, and skip bottom row of numbers

    for i in range(linecount-2, -1, -1):
        # split line by groups of 4 chars
        if stacks_start[i][0:3].strip('[').strip(' ').strip(']') != '':
            stack_1.append(stacks_start[i][0:3].strip('[').strip(' ').strip(']'))
        if stacks_start[i][4:7].strip('[').strip(' ').strip(']'):
            stack_2.append(stacks_start[i][4:7].strip('[').strip(' ').strip(']'))
        if stacks_start[i][8:11].strip('[').strip(' ').strip(']'):
            stack_3.append(stacks_start[i][8:11].strip('[').strip(' ').strip(']'))
        if stacks_start[i][12:15].strip('[').strip(' ').strip(']') != '':
            stack_4.append(stacks_start[i][12:15].strip('[').strip(' ').strip(']'))
        if stacks_start[i][16:19].strip('[').strip(' ').strip(']') != '':
            stack_5.append(stacks_start[i][16:19].strip('[').strip(' ').strip(']'))
        if stacks_start[i][20:24].strip('[').strip(' ').strip(']') != '':
            stack_6.append(stacks_start[i][20:24].strip('[').strip(' ').strip(']'))
        if stacks_start[i][25:28].strip('[').strip(' ').strip(']') != '':
            stack_7.append(stacks_start[i][25:28].strip('[').strip(' ').strip(']'))
        if stacks_start[i][29:32].strip('[').strip(' ').strip(']') != '':
            stack_8.append(stacks_start[i][29:32].strip('[').strip(' ').strip(']'))
        if stacks_start[i][33:36].strip('[').strip(' ').strip(']') != '':
            stack_9.append(stacks_start[i][33:36].strip('[').strip(' ').strip(']'))

    # put stacks into a dictionary - tried to combine this with step above but got confused.
    stack = {}
    stack[1], stack[2], stack[3], stack[4], stack[5], stack[6], stack[7], stack[8], stack[9] = stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9

    # now clean instructions into number of crates to move and from and to stacks
    for line in data:
        if 'move' in line:
            num_to_move = int(line.split(' ')[1])
            move_from = int(line.split(' ')[3])
            move_to = int(line.split(' ')[5])
            crates = []
            # pop crates off the top and add to a list
            for i in range(num_to_move):
                crates.append(stack[move_from].pop())
            # add list items back to stack in reverese order
            for i in range(len(crates)-1,-1,-1):
                stack[move_to].append(crates[i])

    #which crates are at the top of each stack
    top_crates = []
    for i in range(1,10):
        top_crates.append(stack[i].pop())

    return top_crates


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d05-input.txt')
print('Part 1: After the rearrangement procedure completes, what crate ends up on top of each stack?', part_1(data))
print('Part 2: After the rearrangement procedure completes, what crate ends up on top of each stack?', part_2(data))