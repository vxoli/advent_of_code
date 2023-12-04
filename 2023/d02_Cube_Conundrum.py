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

# PART 2
""" data = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'] """
sum = 0
for line in data:
    print(line)
    max_red = max_blue = max_green = 0
    possible = True
    game_number = line.split(":")[0].split(" ")[1]
    game_draw = line.split(":")[1].split(";")
    for play in game_draw:
        cubes = play.lstrip(" ").split(", ")
        print(cubes)
        red_cubes = int(max([x.split(" ")[0] if x.split(" ")[1] == "red" else "0" for x in cubes]))
        blue_cubes = int(max([x.split(" ")[0] if x.split(" ")[1] == "blue" else "0" for x in cubes]))
        green_cubes = int(max([x.split(" ")[0] if x.split(" ")[1] == "green" else "0" for x in cubes]))
        max_red = max(red_cubes, max_red)
        max_blue = max(blue_cubes, max_blue)
        max_green = max(green_cubes, max_green)
    print(max_red,max_green,max_blue)
    power = max_red * max_blue * max_green
    sum += power
    print(power, sum)
print(sum)        