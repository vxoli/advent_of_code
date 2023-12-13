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
while i < 12:
    direction = list(directions.keys())[i%4]
    i += 1
    print(nextPipe, direction)
    nextPipe = data[row+directions[direction][0]][col+directions[direction][1]]
    match direction:
    #if direction == 'U':
        # only | 7 F are valid
        case 'U':
            match nextPipe:
                case '|':
                    print("U&|")
                    row -= 1
                    col = col
                    pipe = nextPipe
                    nextPipe = data[row][col]
                case '7':
                    print("U&7")
                    col = col
                    row += 1
                case 'F':
                    print("F") 
    #if direction == 'R':
        # only - 7 J  are valid
        case 'R':
            match nextPipe:
                case '7':
                    print("R&7")
                    row += 1
                    col += 1
                    pipe = nextPipe
                    nextPipe = data[row][col]
                    print("***",pipe, nextPipe,row,col)
                case 'F':
                    print('J')
                case '-':
                    print("R&-")
                    row = row
                    col += 1
                    pipe = nextPipe
                    nextPipe = data[row][col]
                    print("***",pipe, nextPipe,row,col)                                        
    #if direction == 'D':
        # only | L J are valid
        case 'D':
            match nextPipe:
                case "|":
                    print("D&|")
                    row += 1
                    col = col
                    pipe = nextPipe
                    nextPipe = data[row][col]
                case 'L':
                    print("D&L")
                case 'J':
                    print("D&J")
                    row += 1
                    col -= 1
                    pipe = nextPipe
                    nextPipe = data[row][col]
    #if direction == 'L':
        # only - F L are valid
        case 'L':
            match nextPipe:
                case "-":
                    print("-")
                case "F":
                    print("F")
                case "L":
                    print("L")
                    row = row
                    col -= 1
                    pipe = nextPipe
                    nextPipe = data[row][col]
 
# once back to S count number of moves and divide by 2.
print(i, nextPipe)