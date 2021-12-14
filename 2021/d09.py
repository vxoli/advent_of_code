def read_data(filename):
	with open(filename) as file:
		data = file.readlines()
	return data

# main
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d09-input.txt')