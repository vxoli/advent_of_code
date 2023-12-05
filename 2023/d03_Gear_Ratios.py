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
deltas = [(-1,-1),(0,-1),(+1,-1),(-1,0),(0,0),(+1,0),(-1,+1),(0,+1),(+1,+1)]
for row, line in enumerate(data):
    # Look for a number
    number = ""
    columnStart = columnEnd = -1
    for column, char in enumerate(line):
        if char.isnumeric():
            number += char
            columnStart = (column * (columnStart == -1)) + ((columnStart != -1) * min(columnStart, column))
            
        else:
            columnEnd = columnStart + len(number) - 1 
            if number != "": # a number has been found
                # columnEnd = column-1
                # now search around number
                print(number,columnStart,columnEnd)
                y = row
                isPartNumber = False
                for x in range(columnStart, columnEnd+1):
                    for delta in deltas:
                        new_x = x + int(delta[0])
                        new_y = y + int(delta[1])
                        print(x,y,new_x, new_y)
                        if new_x < 0 or new_x > len(line)-1: continue
                        if new_y < 0 or new_y > len(data)-1: continue
                        print(data[new_y][new_x],isPartNumber)
                        if data[new_y][new_x] in ['$','*','+','#']: 
                            isPartNumber = True
                            print(number,"is a partnumber")
                            break

                if isPartNumber == True:
                        break

                    
                number = ""
                columnStart = columnEnd = -1

                    
                

    # find start and end coordinated of number
    # look for symbols around number
    # if symbol add to sum
    # if no symbol ignore
