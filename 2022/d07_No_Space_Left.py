# AoC 2022
# --- Day 07 No Space Left on Device ---

import urllib.request
from collections import defaultdict
from itertools import accumulate

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
	sizes = defaultdict(int)
	stack = []
	for line in data:
		if line.startswith('$ ls') or line.startswith('dir'):
			continue
		
		match line.split():
			case "$", 'cd', '..':
				stack.pop()
			case '$', 'cd', directory:
				stack.append(directory)
			case size, _:
				for path in accumulate(stack, func=lambda a,b: a+"/"+b):
					sizes[path] += int(size)
			
	return (sum(size for size in sizes.values() if size <= 100000))


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d07-input.txt')
print(part_1(data))