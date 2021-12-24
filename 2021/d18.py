# AoC 2021 d18
# --- Day 18: Snailfish ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data


# MAIN
data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d18-input.txt')

