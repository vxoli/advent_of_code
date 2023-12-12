# --- Day 9: Mirage Maintenance ---

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
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d09_input.txt")
# convert strings to int
for i, line in enumerate(data):
    newline = [eval(x) for x in line.split(" ")]
    data[i] = newline

# PART 1
# data = [[0, 3, 6, 9, 12, 15,],[1, 3, 6, 10, 15, 21],[10, 13, 16, 21, 30, 45]]
total = 0
for line in data:
    index = 0
    differences = []
    lastDiff = 0
    differences.append(line)
    while sum(differences[(index)*(index>0)]) > 0:
        differences.append([differences[index][i+1]-differences[index][i] for i in range(len(differences[index])-1)])
        lastDiff = differences[index][-1]
        index += 1
    predictedNext = 0
    newDiff = lastDiff
    for i in reversed(differences[0:len(differences)-1]):
        predictedNext = newDiff + i[-1]
        newDiff = predictedNext
    total += predictedNext-lastDiff
print(total)