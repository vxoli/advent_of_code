# Day 03: Gear Ratios

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
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d03_input.txt")
data = ['467..114..',
'...*......',
'..35..633.',
'......#...',
'17*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']

# PART 1
directions = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)]
for row, line in enumerate(data):
    # Look for a number
    number = ""
    columnStart = columnEnd = -1
    for column, char in enumerate(line):
        if char.isnumeric():
            print(char,column)
            number += char
            columnStart = (column * (columnStart == -1)) + ((columnStart != -1) * min(columnStart, column))
            
        else:
            if number != "": # a number has been found
                columnEnd = column-1
                print(number, columnStart, columnEnd)
                number = ""
                columnStart = columnEnd = -1
                # now search around number 
                

    # find start and end coordinated of number
    # look for symbols around number
    # if symbol add to sum
    # if no symbol ignore
