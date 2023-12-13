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
        print(direction, nextPipe)
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
                    row = row
                    col += 1
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
    print(row, col, pipe)
    return(row, col, pipe)

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d10_input.txt")
data = ['.....','.S-7.','.|.|.','.L-J.','.....']
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
i=0
# look for valid 1st pipe off starting point
row,col,pipe = startMove(rowS, colS, 'S')

# now follow the route
while i < 10:
    match pipe:
        case '-':
            row =row
            col += 1
        case '|':
            row += 1
            col = col
        case 'L':
            row += 1
            col += 1
        case 'J':
            row = row
            col -= 1
        case '7':
            row += 1
            col = col
        case 'F':
            row -= 1
            col += 1
    pipe = data[row][col]
    print(row,col,pipe,i)
    i += 1

        
            
# once back to S count number of moves and divide by 2.
