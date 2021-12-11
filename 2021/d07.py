#AoC 2021 d07.py

from statistics import mode, mean, median

def read_data(filename):
	with open(filename, 'r') as file:
		data = [int(x) for x in file.read().split(',')]
	return data

def part1(position_data):
	# median is value with least total differences
	median_position = round(median(position_data),0)
	fuel_sum = 0
	difference = 0
	for position in position_data:
		difference = abs(position - median_position)
		fuel_sum += difference
	return fuel_sum

def part2(position_data):
	#now mean is value with least total differences

	mean_position = round(mean(position_data),0)
	fuel_sum = 0
	difference = 0
	maxl=max([abs(int(i)) for i in  position_data])
	return int(min([sum([(abs(int(i)-j)+1)*(abs(int(i)-j))/2 for i in  position_data]) for j in range(maxl)]))

# MAIN
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d07-input.txt')
print("Part 1: How much fuel must they spend to align to that position? ", part1(input_data))
print("Part 2: How much fuel must they spend to align to that position? ", part2(input_data))
