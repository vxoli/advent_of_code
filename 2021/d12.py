# AoC 2021 d12
# --- Day 12: Passage Pathing ---

import urllib.request

def read_file(filename):
	with open(filename) as file:
		data = file.read().strip()
	file.close()
	data = data.split("\n")
#	data = [list(map(int, line)) for line in data]
	return data

def read_url():
	file = urllib.request.urlopen('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d12-input.txt')
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	return data

def part1_count(node, visited = set()):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next in visited: continue
        total += part1_count(next, visited | {node} if node == node.lower() else visited)
    return total

def part2_count(node, visited = set(), double_visit = False):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
    	if next == "start": continue
    	if next in visited and double_visit: continue
    	if next in visited:
    		total += part2_count(next, visited | {node} if node == node.lower() else visited, True)
    	else:
    		total += part2_count(next, visited | {node} if node == node.lower() else visited, double_visit)
    return total


# MAIN
input_data = read_url()

edges = {}

for line in input_data:
    a, b = line.split("-")
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

print("Part 1: How many paths through this cave system are there that visit small caves at most once? ", part1_count("start"))
print("Part 2: How many paths through this cave system are there? ", part2_count("start"))