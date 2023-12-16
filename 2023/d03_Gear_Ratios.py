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
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']

# PART 1
# search across each row - if a number found then look for symbols above or below or next to it.
# if no numbers - ignore
# if there are numbers add the number to the total

print(data)
numbers = []
for y,row in enumerate(data):
    numStr = ""
    for x,char in enumerate(row):
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            numStr += char
        if char in ['.','!','@','#','$','%','^','&','*','(',')'] and numStr != "":
            numbers.append(numStr)
            numStr = ""
 
    print(numbers)