# Aoc 2021 d04

def read_data(filename):
	with open(filename) as file:
		data = [line.strip('\n') for line in list(file)]
	file.close()
	#strip the newlines '\n'
	data = [line.strip('') for line in data]

	return data

def split_data(data): # split given data into game numbers and boards
	game_numbers = data[0]
	board_numbers = data[2:]

	#split the boards into array of n boards
	boards = [[0] *5] * 100
	board_counter = 0

	for index in range(len(board_numbers)):
		if board_numbers[index] == '': 
			board_counter += 1
			continue
		boards[board_counter][index%6] = board_numbers[index]
		print(index, "---",index % 6, "---", board_counter, board_numbers[index])

	return (game_numbers, boards)

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d04-input.txt')
print(input_data)
#split the given data in to game numbers drawn and boards
numbers, boards = split_data(input_data)
print(numbers)
print(boards[0][0:])