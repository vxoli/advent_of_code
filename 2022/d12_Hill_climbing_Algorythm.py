# AoC 2022
# --- Day 12: Hill Climbing Algorithm ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):

	return

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d12-input.txt')
print(input)