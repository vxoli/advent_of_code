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
