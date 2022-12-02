# D02 AoC 2022 Rock paper Scissors

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines


input = read_data('/home/christopher-spectre/Documents/code/adventofcode/2022/d02-input.txt')
print(input)
