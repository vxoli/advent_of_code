#Aoc @022
# --- Day 10: Cathode-Ray Tube ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(instructions):
	cycle, prev_cycle = 1,1
	x, prev_x = 1,1
	sum_signal_strengths = 0
	for line in instructions:
		command = line.split(' ')[0]
		match command:
			case 'noop':
				cycle += 1
				if cycle in [20,60,100,140,180,220]:
					sum_signal_strengths += cycle * x
			case 'addx':
				cycle += 1
				if cycle in [20,60,100,140,180,220]:
					sum_signal_strengths += cycle * x
				cycle += 1
				x += int(line.split(' ')[1])
				if cycle in [20,60,100,140,180,220]:
					sum_signal_strengths += cycle * x

		prev_x, prev_cycle = x,cycle

	return sum_signal_strengths

def part_2(instructions):
# do not uderstand Part 2 of the problem. :-(
	return

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d10-input.txt')
# data = ['addx 15','addx -11','addx 6','addx -3','addx 5','addx -1','addx -8','addx 13','addx 4','noop','addx -1','addx 5','addx -1','addx 5','addx -1','addx 5','addx -1','addx 5','addx -1','addx -35','addx 1','addx 24','addx -19','addx 1','addx 16','addx -11','noop','noop','addx 21','addx -15','noop','noop','addx -3','addx 9','addx 1','addx -3','addx 8','addx 1','addx 5','noop','noop','noop','noop','noop','addx -36','noop','addx 1','addx 7','noop','noop','noop','addx 2','addx 6','noop','noop','noop','noop','noop','addx 1','noop','noop','addx 7','addx 1','noop','addx -13','addx 13','addx 7','noop','addx 1','addx -33','noop','noop','noop','addx 2','noop','noop','noop','addx 8','noop','addx -1','addx 2','addx 1','noop','addx 17','addx -9','addx 1','addx 1','addx -3','addx 11','noop','noop','addx 1','noop','addx 1','noop','noop','addx -13','addx -19','addx 1','addx 3','addx 26','addx -30','addx 12','addx -1','addx 3','addx 1','noop','noop','noop','addx -9','addx 18','addx 1','addx 2','noop','noop','addx 9','noop','noop','noop','addx -1','addx 2','addx -37','addx 1','addx 3','noop','addx 15','addx -21','addx 22','addx -6','addx 1','noop','addx 2','addx 1','noop','addx -10','noop','noop','addx 20','addx 1','addx 2','addx 2','addx -6','addx -11','noop','noop','noop']

print("Part 1: What is the sum of these six signal strengths?",part_1(data))