# Aoc 2021 d04

def read_data(filename):
	with open(filename) as file:
		data = [line.strip('\n') for line in list(file)]
	file.close()
	# #strip the newlines '\n'
	# data = [line.strip('') for line in data]

	return data

def split_data(data): # split given data into game numbers and boards
	game_numbers = data[0]
	board_numbers = data[2:]

	#split the boards into array of n boards
	board = [[0] * 7 for i in range(100)]
	board_counter = 0

	for index in range(len(board_numbers)):
		if board_numbers[index] == '': 
			board_counter += 1
			continue
	
		# board[0] = board number
		# board[1] = true/ false - has the board been solved
		# board[2-7] = lists of 5 numbers for each row
		board[board_counter][0] = board_counter
		# strip out spaces and double spaces (for single digit numbers) by converting ' ' and '  ' to '!' then strip '!'
		board[board_counter][2 + index % 6] = list(board_numbers[index].replace('  ', '!').replace(' ','!').split('!'))	

	return (game_numbers, board)

def play_bingo():
# an idea to play
# if a number on board - that number knocked out or converted to 999 say
# if an elemenet of list is all 999 - a row copleted
# a nested for loop can check if columns all 999
# if a solution found flag with board[1] set to true/ 1

	return

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d04-input.txt')
#split the given data in to game numbers drawn and boards
(numbers, boards) = split_data(input_data)
# play bingo
play_bingo()