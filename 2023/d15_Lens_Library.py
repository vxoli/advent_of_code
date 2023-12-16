# --- Day 15: Lens Library ---

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
sequence = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d15_input.txt")
# sequence = ['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7']
# sequence = ['HASH']
sequence = sequence[0].split(',')
sum = 0
for step in sequence:
    value = 0
    for char in step:
        value += ord(char)
        value *= 17
        value = value % 256
    sum += value
print("Part 1: What is the sum of the results?", sum)
