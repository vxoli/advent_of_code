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

def startMove(row, col, pipe):
    for direction in list(directions.keys()):
        nextPipe = data[row+directions[direction][0]][col + directions[direction][1]]
        # if valid move then store and break loop
        if direction == 'U' and nextPipe in ['|','7','F']:
            match nextPipe:
                case '|':
                    row -= 1
                    col = col
                    pipe = nextPipe
                case '7':
                    row -= 1
                    col -= 1
                    pipe = nextPipe
                case 'F':
                    row -=1
                    col += 1
                    pipe = nextPipe
            break
        if direction == 'R' and nextPipe in ['-','7']:
            match nextPipe:
                case '-':
                    row = row
                    col += 1
                    pipe = nextPipe
                case '7':
                    row += 1 
                    col += 1
                    pipe = nextPipe
            break
        if direction == 'D' and nextPipe in ['|','J','L']:
            match nextPipe:
                case '|':
                    row += 1
                    col = col
                    pipe = nextPipe
                case 'J':
                    row -= 1
                    col += 1
                    pipe = nextPipe
                case 'L':
                    row += 1
                    col += 1
                    pipe = nextPipe
            break
        if direction == 'L' and nextPipe in ['-', 'F']:
            match nextPipe:
                case '-':
                    row = row
                    col -= 1
                    pipe = nextPipe
            break
    pipe = nextPipe
    return(row, col, pipe, direction)

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d10_input.txt")
#data = ['.....','.S-7.','.|.|.','.L-J.','.....']
#data = ['7-F7-','.FJ|7','SJLL7','|F--J','LJ.LJ']
# define movements in a dict (pipe : (dx,dy))
pipes = dict([('|',(0,1)),('-',(1,0)),('L',(1,0)),('J',(-1,0)),('7',()),('F',()),('.',()),('S',())])
directions = dict([('U',(-1,0)), ('R', (0,1)), ('D', (1,0)), ('L', (0,-1))])
# find the starting point: store co-ords in list
for row, line in enumerate(data):
    if 'S' in line:
        rowS = row
        colS = line.index('S')
pipe = [('S',(rowS,colS))]
nextPipe = ""
# scan around clockwise and find next possible connected pipe
# move to next point based - store co-ordinates etc...
row = rowS
col = colS
i=1
# look for valid 1st pipe off starting point
row,col,pipe, lastMove = startMove(rowS, colS, 'S')
# now follow the route
while (pipe != 'S'):

    match pipe:
        case '-':
            if lastMove == 'R':
                row = row
                col += 1
            if lastMove == 'L':
                row = row
                col -= 1
        case '|':
            if lastMove == 'D':
                row += 1
                col = col
            if lastMove == 'U':
                row -= 1
                col = col
        case 'L':
            if lastMove == 'D':
                row = row
                col += 1
                lastMove = 'R'
            if lastMove == 'L':
                row -= 1
                col = col
                lastMove = 'U'            
        case 'J':
            if lastMove == 'D':
                row = row
                col -= 1
                lastMove = 'L'
            if lastMove == 'R':
                row -= 1
                col = col
                lastMove = 'U'
        case '7':
            if lastMove == 'R':
                row += 1
                col = col
                lastMove = 'D'
            if lastMove == 'U':
                row = row
                col -= 1
                lastMove = 'L'
        case 'F':
            if lastMove == 'U':
                row = row
                col += 1
                lastMove = 'R'
            if lastMove == 'L':
                row += 1
                col = col
                lastMove = 'D'
    pipe = data[row][col]
    i += 1

        
            
# once back to S count number of moves and divide by 2.
print("Part 1: How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?", int(i/2))
