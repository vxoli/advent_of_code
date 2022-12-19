# AoC 2022
# --- Day 17: Pyroclastic Flow ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d17-input.txt')