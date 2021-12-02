# AoC 2021 D01

def read_data(filename):
	with open(filename) as file:
		lines = list(map(int, file.readlines()))
	file.close()

	return lines


def part1(lines):
	counter = 0
	for index, line in enumerate(lines):
		if index + 1 == len(lines):
			break
		if line < lines[index+1]:
			counter += 1
	return counter

def part2(lines):
	counter = 0
	for index, line in enumerate(lines):
		if index + 3 == len(lines):
			break
		if line + lines[index+1] + lines[index+2] < lines[index+1] + lines[index+2] + lines[index+3]:
			counter += 1
	return counter


input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d01-input.txt')
print("Answer part 1: ", part1(input_data))
print("Answer part 2: ", part2(input_data))