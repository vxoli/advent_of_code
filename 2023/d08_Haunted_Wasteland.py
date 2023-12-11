# --- Day 8: Haunted Wasteland ---

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
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d08_input.txt")
# data = ['RL','','AAA = (BBB, CCC)', 'BBB = (DDD, EEE)','CCC = (ZZZ, GGG)','DDD = (DDD, DDD)','EEE = (EEE, EEE)','GGG = (GGG, GGG)','ZZZ = (ZZZ, ZZZ)']
# data = ['LLR', '', 'AAA = (BBB, BBB)', 'BBB = (AAA, ZZZ)', 'ZZZ = (ZZZ, ZZZ)']
moves = data [0]
data = data[2:-1]
map = dict([(x.split(' = ')[0], x.split(' = ')[1]) for x in data])
locationList = [x.split(' = ')[0] for x in data]
location = locationList[0]
index = steps = 0
while location != 'ZZZ':
    move = moves[index]
    index = (index+1) * (index+1 < len(moves))
    location = map[location].strip('(').strip(')').split(', ')[0 + (move=='R')]
    steps += 1
print("Part 1: Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?",steps)