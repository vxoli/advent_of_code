# AoC 2021 D02

def read_data(filename):
	with open(filename) as file:
		lines = file.readlines()
	file.close()

	return lines

def part1(instructions):
	depth = 0
	horizontal = 0
	for line in instructions:
		command = line.split()[0]
		value = int(line.split()[1])
		if command == 'forward':
			horizontal += value
		if command == 'down':
			depth += value
		if command == 'up':
			depth -= value
	return horizontal * depth

def part2(instructions):
	depth = 0
	horizontal = 0
	aim = 0
	for line in instructions:
		command = line.split()[0]
		value = int(line.split()[1])
		if command == 'forward':
			horizontal += value
			depth += aim * value
		if command == 'down':
			aim += value
		if command == 'up':
			aim -= value
	return horizontal * depth

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d02-input.txt')
print("Part 1 answer: ", part1(input_data))
print("Part 2 answer: ", part2(input_data))