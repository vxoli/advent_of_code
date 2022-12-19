# AoC 2022
# --- Day 16: Proboscidea Volcanium ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d16-input.txt')
for line in input: print(line)
