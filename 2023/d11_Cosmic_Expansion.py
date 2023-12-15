# --- Day 11: Cosmic Expansion ---

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
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d11_input.txt")
data = ['...#......',
'.......#..',
'#.........',
'..........',
'......#...',
'.#........',
'.........#',
'..........',
'.......#..',
'#...#.....']
# look for rows with no galaxies and double
universe = []
for row in data:
    universe.append(row)
    if '#' not in row:
        universe.append(row)
# rotate 90 degrees
rotated = list(zip(*universe[::-1]))
# look for rows with no galaxies again and double them
universe = []
for row in rotated:
    universe.append(row)
    if '#' not in row:
        universe.append(row)
# rotate back
universe = list(zip(*universe))[::-1]
# now have each point in universe as a tuple
# convert tuples back to list of strings
newUniverse = []
for row in universe:
    newUniverse.append(''.join(row))
# count universes and store location in dict (n: (x,y))
i = 1
galaxies = dict()
for n,row in enumerate(newUniverse):
    for m, char in enumerate(row):
        if char == "#":
            galaxies[i] = (n,m)
            i += 1
print(n,galaxies)
# iterate over pairs
# calculate distance between min (dx+dy),(dy+dx)
# keep total sum