#AoC 2022
# --- Day 06: Tuning Trouble ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def find_marker(data, num):
	buffer = data[0]
	marker = ""
	num -= 1
	for i, character in enumerate(buffer[num:]): #start loop at 14th letter
		position = i + num
		marker = buffer[position-num:position+1]
		# check if letters repeated in marker - 
		if len(set(marker)) == len(marker):
			return position + 1 
	return

	return

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d06-input.txt')
print('Part 1: How many characters need to be processed before the first start-of-message marker is detected?',find_marker(data,4))
print('Part 2: How many characters need to be processed before the first start-of-message marker is detected?',find_marker(data,14))