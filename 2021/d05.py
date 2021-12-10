# AoC 2021 d05

def read_data(filename):
	with open(filename) as file:
		data = [line.strip('\n') for line in list(file)]
	file.close()

	return data


input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d05-input.txt')
print(input_data[1].split(' -> '))
