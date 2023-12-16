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
data =['O....#....',
'O.OO#....#,'
'.....##...',
'OO.#O....O',
'.O.....O#.',
'O.#..O.#.#',
'..O..#O..O',
'.......O..',
'#....###..',
'#OO..#....']
# store map in dict of co-ordinates key = (x,y) value = char
numRows = len(data)
numCols = len(data[0])
map = dict()
map = {(i, j): char for i, row in enumerate(data) for j, char in enumerate(row)}
