# --- Day 10: Pipe Maze ---

import urllib.request

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    return data

def read_data(filename):
    with open(filename) as file:
        lines = list(map(str, file.readlines()))
    file.close()
    return lines

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d10_input.txt")
data = ['.....','.S-7.','.|.|.','.L-J.','.....']
# define movements in a dict (pipe : (dx,dy))
pipes = dict([('|',(0,1)),('-',(1,0)),('L',(1,0)),('J',(-1,0)),('7',()),('F',()),('.',()),('S',())])
directions = dict([('U',(0,-1)), ('UR', (-1,1)), ('R', (1,0)), ('DR', (1,1)), ('D', (0,1)), ('DL', (1,-1)), ('L', (0,-1)), ('UL',(-1,-1))])
# find the starting point: store co-ords in list
for row, line in enumerate(data):
    if 'S' in line:
        rowS = row
        colS = line.index('S')
# scan around clockwise and find next possible connected pipe
# move to next point based - store co-ordinates etc...
for direction in directions.keys():
    print(directions[direction])


# once back to S count number of moves and divide by 2.
