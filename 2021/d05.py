# AoC 2021 d05

def read_data(filename):
	with open(filename) as file:
		data = [line.strip('\n') for line in list(file)]
	file.close()
	return data

def part1(coordinates):
	for line in coordinates:
		x1 = int(line.split(' -> ')[0].split(',')[0])
		y1 = int(line.split(' -> ')[0].split(',')[1])
		x2 = int(line.split(' -> ')[1].split(',')[0])
		y2 = int(line.split(' -> ')[1].split(',')[1])


	return

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d05-input.txt')
print(input_data[1].split(' -> '))
part1(input_data)