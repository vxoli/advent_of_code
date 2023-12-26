# Day 03: Gear Ratios - take 2

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
grid = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d03_input.txt")
grid = ['467..114..',
'...*......',
'..35..633.',
'......#...',
'17*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']

cs = set()
for r, row in enumerate(grid):
    for c,char in enumerate(row):
        if char.isdigit() or char ==".":
            continue
        for dr in range(r-1,r+2):
            for dc in range(c-1,c+2):
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc-1].isdigit():
                    dc -= 1
                cs.add((dr,dc))
ns = []
for r,c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))
print(sum(ns))

# Part 2
total = 0
for r, row in enumerate(grid):
    for c,char in enumerate(row):
        if char !="*":
            continue
        cs = set()

        for dr in range(r-1,r+2):
            for dc in range(c-1,c+2):
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc-1].isdigit():
                    dc -= 1
                cs.add((dr,dc))
        if len(cs) != 2: continue
        
        ns = []
        for r,c in cs:
            s = ""
            while c < len(grid[r]) and grid[r][c].isdigit():
                s += grid[r][c]
                c += 1
            ns.append(int(s))
        total += ns[0]*ns[1]
print(total)
