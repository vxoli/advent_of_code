#AoC 2022
# --- Day 06: Tuning Trouble ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
	buffer = data[0]
	marker = ""
	for i, character in enumerate(buffer[3:]): #start loop at 4th letter
		position = i + 3
		marker = buffer[position-3:position+1]
		# check if letters repeated in marker - 
		a = list(set(marker))
		b = list(marker)
		a.sort()
		b.sort()
		if a == b:
			return position + 1 

	return

def part_2(data):
	buffer = data[0]
	marker = ""
	for i, character in enumerate(buffer[13:]): #start loop at 14th letter
		position = i + 13
		marker = buffer[position-13:position+1]
		# check if letters repeated in marker - 
		a = list(set(marker))
		b = list(marker)
		a.sort()
		b.sort()
		if a == b:
			return position + 1 
	return

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d06-input.txt')
print('Part 1: How many characters need to be processed before the first start-of-message marker is detected?',part_1(data))
print('Part 2: How many characters need to be processed before the first start-of-message marker is detected?',part_2(data))