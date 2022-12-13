# AoC 2022
# --- Day 13: Distress Signal  ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):

	return

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d13-input.txt')
print(input)