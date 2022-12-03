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
    #define starting variables
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

def part_2(data):
    # loop through the dataset three lines at a time
    # search each of the three lines for a like letter
    # determine the priority value for the letter
    # keep a running total of the priorities

    # define starting variables
    match = ""
    prioritysum = 0
    # setup dict of priority values
    priorities = dict()
    for index, letter in enumerate(string.ascii_lowercase+string.ascii_uppercase):
        priorities[letter] = index + 1

    # loop through dataset 3 lines at a time
    for line in range(0, len(data), 3):
        line1 = data[line]
        line2 = data[line+1]
        line3 = data[line+2]

        for i in line1:
            for j in line2:
                if i == j:
                    for k in line3:
                        if j == k:
                            badge = i
                            break
        prioritysum += priorities[badge]

    return prioritysum

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d03-input.txt')
print("Part 1: What is the sum of the priorities of those item types?", part_1(data))
print("Part 2: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?", part_2(data))