# AoC 2022
# --- Day 4: Camp Cleanup ---
import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
    counter = 0 
    # In how many assignment pairs does one range fully contain the other?
    for pair in data:
        elf1_assigned = ""
        elf2_assigned = ""
        elf1,elf2 = pair.split(',')
        elf1_start,elf1_end = map(int, elf1.split('-'))
        elf2_start,elf2_end = map(int, elf2.split('-'))

        # the areas IDs will be contained if 1_start >= 2_start and 1_end <= 2_end and vice veras
        if elf1_start >= elf2_start and elf1_end <= elf2_end or elf2_start >= elf1_start and elf2_end <= elf1_end:
            counter += 1

    return counter

def part_2(data):
    # In how many assignment pairs do the ranges overlap?
    counter = 0
    for pair in data:
        elf1_assigned = ""
        elf2_assigned = ""
        elf1,elf2 = pair.split(',')
        elf1_start,elf1_end = map(int, elf1.split('-'))
        elf2_start,elf2_end = map(int, elf2.split('-'))

        if max(elf1_start, elf2_start) <= min(elf1_end, elf2_end):
            counter += 1

    return counter

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d04-input.txt')
print("Part 1: In how many assignment pairs does one range fully contain the other?",part_1(data))
print("Part 2: In how many assignment pairs do the ranges overlap?",part_2(data))