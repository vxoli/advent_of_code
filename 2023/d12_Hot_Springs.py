# --- Day 12: Hot Springs ---

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

def arrangements(conditions, groups, memo={}):
    if len(conditions) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0
 
    if len(groups) == 0:
        if "#" in conditions:
            return 0
        else:
            return 1
    if (conditions, groups) in memo:
        return memo[(conditions, groups)]
    curr, size = conditions[0], groups[0]
    counts = 0
    if curr == "." or curr == "?":
        counts += arrangements(conditions[1:], groups, memo)
    if (
        (curr == "#" or curr == "?")
        and len(conditions) >= size
        and "." not in conditions[:size]
        and (size == len(conditions) or conditions[size] != "#")
    ):
        counts += arrangements(conditions[size + 1 :], groups[1:])
    memo[(conditions, groups)] = counts
    return counts

# MAIN
map = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d12_input.txt")
""" map = ['???.### 1,1,3',
'.??..??...?##. 1,1,3',
'?#?#?#?#?#?#?#? 1,3,1,6',
'????.#...#... 4,1,1',
'????.######..#####. 1,6,5',
'?###???????? 3,2,1'] """
lines = []
answer = 0
for line in map:
    conditions, groups = line.split(" ")
    groups = tuple([int(x) for x in groups.split(",")])
    answer += arrangements(conditions, groups)
print(answer)