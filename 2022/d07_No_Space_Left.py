# AoC 2022
# --- Day 07 No Space Left on Device ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
    print(data)
    return


data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d07-input.txt')
part_1(data)