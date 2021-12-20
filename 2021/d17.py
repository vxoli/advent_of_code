# Aoc 2021 d17
# --- Day 17: Trick Shot ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	return data[0]


# MAIN
input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d17-input.txt')
print(input)