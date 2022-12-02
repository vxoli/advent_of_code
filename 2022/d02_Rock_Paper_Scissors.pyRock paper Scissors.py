# D02 AoC 2022 Rock paper Scissors

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(plays):
    for play in plays:
        elf_play = play.split()[0]
        my_play = play.split()[1]
        print(play.split()[1])
    
    return

input_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d02-input.txt')
print(part_1(input_data))