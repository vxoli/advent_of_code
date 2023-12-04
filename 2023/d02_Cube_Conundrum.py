# Day 2: Cube Conundrum

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
# PART 1
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d02_input.txt")
sum = 0
for line in data:
    possible = True
    game_number = line.split(":")[0].split(" ")[1]
    game_draw = line.split(":")[1].split(";")
    for play in game_draw:
        cubes = play.split(",")
        for cube in cubes:
            number = int(cube.split(" ")[1])
            colour = cube.split(" ")[2]
            if (colour == "red" and number > 12) or (colour == "green" and number > 13) or (colour == "blue" and number > 14):
                possible = False
    sum += int(game_number) * possible

print("What is the sum of the power of these sets?",sum)                
