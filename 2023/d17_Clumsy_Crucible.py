# --- Day 17: Clumsy Crucible ---
import urllib.request, random

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    return data

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d17_input.txt")
data = ['2413432311323','3215453535623','3255245654254','3446585845452','4546657867536','1438598798454','4457876987766','3637877979653','4654967986887','4564679986453','1224686865563','2546548887735','4322674655533']
rows = len(data)-1
cols = len(data[0])-1
start = (0,0)
end = (cols,rows)
position = start
directions = {0:'S', 1:'R', 2:'L'}
compass = {'N':(1,0),'E':(0,1),'S':(-1,0),'W':(0,-1)}
currentDirection = lastThreeMoves = directions[random.randint(0,1)] # can only start straight or right
heatLoss = leastHeatLoss = 0
if currentDirection == 'S': currentDirection = 'E'
if currentDirection == "R": currentDirection = 'S'
while position != end:
    # work out next move and if more than three in a row
    print(lastThreeMoves)
    nextMoveDirection = directions[random.randint(0,2)]
    print(nextMoveDirection)
    lastThreeMoves += nextMoveDirection
    if len(lastThreeMoves) > 4: lastThreeMoves = lastThreeMoves[1:]
    if lastThreeMoves in ["LLLL",'RRRR','SSSS']: 
        print("more than three in a row")
        continue
    # now decide compass direction and change position
    match currentDirection:
        case 'N':
            match nextMoveDirection:
                case 'S':
                    nextDirection = 'N'
                case 'R':
                    nextDirection = 'E'
                case 'L':
                    nextDirection = 'W'
        
        case 'E':
            match nextMoveDirection:
                case 'S':
                    nexttDirection = 'E'
                case 'R':
                    nextDirection = 'S'
                case 'L':
                    nextDirection = 'N'
        case 'S':
            match nextMoveDirection:
                case 'S':
                    nextDirection = 'S'
                case 'R':
                    nextDirection = 'W'
                case 'L':
                    nextDirection = 'E'
        case 'W':
            match nextMoveDirection:
                case 'S':
                    nextDirection = 'W'
                case 'R':
                    nextDirection = 'N'
                case 'L':
                    nextDirection = 'S'
    print(nextDirection)
    print(compass[nextDirection])
    delta = compass[nextDirection]
    position = (position[0]+delta[0], position[1]+delta[1])

    print(lastThreeMoves)
    print(position, delta)
    if position[0] > cols or position[1] > rows or position[0] < 0 or position[1] < 0:
        position = (position[0]-delta[0], position[1]-delta[1])
        continue

    heatLoss += int(data[position[0]][position[1]])
print(heatLoss)