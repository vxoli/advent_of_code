# --- Day 14: Parabolic Reflector Dish ---

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

# MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d14_input.txt")
""" data =['O....#....',
'O.OO#....#',
'.....##...',
'OO.#O....O',
'.O.....O#.',
'O.#..O.#.#',
'..O..#O..O',
'.......O..',
'#....###..',
'#OO..#....']
 """# store map in dict of co-ordinates key = (x,y) value = char
numRows = len(data)
numCols = len(data[0])
map = dict()
map = {(i, j): char for i, row in enumerate(data) for j, char in enumerate(row)}
# start from north edge and move south
# if find a O rock see if can roll north to a '.'. If north place contatins 'O' or '#' can roll.
# if rolls replace with empty '.'
for i in range (numRows-2):
    for y in range (1,numRows):
        for x in range(numCols):
            if map[(y,x)] == "O" and map[(y-1,x)] ==".":
                map[(y-1,x)] = "O"
                map[(y,x)] = '.'
# assign the loading to the rows and sum
loadTotal = 0
for y in range(numRows):
    rowOcount = 0
    for x in range(numCols):
        if map[(y,x)] == "O":
            rowOcount += 1
    loadTotal += rowOcount * (numRows-y)
print("Part 1: what is the total load on the north support beams?", loadTotal)