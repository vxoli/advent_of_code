#AoC 2021 d07.py

from statistics import mode, mean, median

def read_data(filename):
	with open(filename, 'r') as file:
		data = [int(x) for x in file.read().split(',')]
	return data

def part1(position_data):
	#try this:
	# determine mode
	# deterine differences from position to mode
	# sum the differences to find amount of fuel

	median_position = round(median(position_data),0)
	fuel_sum = 0
	difference = 0
	for position in position_data:
		difference = abs(position - median_position)
		fuel_sum += difference
	return fuel_sum

# MAIN
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d07-input.txt')
print("Part 1: How much fuel must they spend to align to that position? ", part1(input_data))

