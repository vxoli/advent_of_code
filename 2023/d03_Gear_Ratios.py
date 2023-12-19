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
""" data = ['467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..'] """

# PART 1
# find the symbols in teh data set and store in a set
symbols = {char for row in data for char in row if not char.isnumeric()}
# search across each row - if a number found then add to list with co-ordinates
numbers = []
for y,row in enumerate(data):
    numStr = ""
    for x,char in enumerate(row):
        if char.isnumeric():
            numStr += char
        if char in symbols and numStr != "":
            numbers.append((numStr,(x-len(numStr),y)))
            numStr = ""
 
# now look for symbols above or below or next to the numbers.
# if there are symbols add the number to the total
total = 0
#symbols.discard('.') # need to drop the '.' from the symbols set
for value in numbers:
    number = value[0]
    coords = value[1]
    xStart = coords[0]
    xEnd = xStart+len(number)-1
    y = coords[1]
    xStart = ((xStart -1)>=0) * (xStart-1) + ((xStart -1) <0) * 0
    xEnd = ((xEnd +1) > (len(data[0])-1) * (xEnd)) + (((xEnd +1) <= len(data[0])-1) * (xEnd+1))
    yStart = ((y-1)>=0)*(y-1) + ((y-1)<0)*0 
    yEnd = ((y+1)<=len(data)-1)*(y+1) + ((y+1)>len(data)-1)*y
    total += sum(int(number) for y in range(yStart, yEnd + 1) for x in range(xStart, xEnd + 1) if data[y][x] in symbols)

print("Part 1: What is the sum of all of the part numbers in the engine schematic?",total)