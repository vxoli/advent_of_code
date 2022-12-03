# AoC 2022
# Day 3: Rucksack Reorganization

import urllib.request
import string

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(data):
    match = ""
    prioritysum = 0
    # setup dict of priority values
    priorities = dict()
    for index, letter in enumerate(string.ascii_lowercase+string.ascii_uppercase):
        priorities[letter] = index + 1

    for line in data:
        # split bag into two compartments
        compartment1 = line[:int(len(line)/2)]
        compartment2 = line[int(len(line)/2):]
        # look for the matching letter in each compartment
        for i in compartment1:
            for j in compartment2:
                if i == j:
                    match = i
                    break

        # update prioritysum with prioriity value
        prioritysum += priorities[match]

    return prioritysum

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d03-input.txt')
print("Part 1: What is the sum of the priorities of those item types? ", part_1(data))