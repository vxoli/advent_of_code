#Aoc 2021 d08

def read_data(filename):
	with open(filename) as file:
		data = file.readlines()

	return data

def part1(codes):
	# loop through all codes in list
	# split line at |
	# 1 has 2 codes, 4 uses 4 codes, 7 uses 3 codes, 8 uses all 7 codes.
	# count the number of times a 2/4/3 or 7 letter code appears
	# return answer
	counter = 0
	for line in codes:
		output_code = line.split('|')[1]
		for each_code in output_code.split(' '):
			if len(each_code.strip()) in {2,4,3,7}:
				counter += 1
	return counter

#main
input_data = read_data("/home/christopher/Documents/GitHub/adventofcode/2021/d08-input.txt")
print("Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear? ", part1(input_data))