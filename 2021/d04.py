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

	# need to clean numbers
	game_numbers = game_numbers.split(',')

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
	print(board_counter)
	print(game_numbers)
	return (game_numbers, board)

def play_bingo(bingo_numbers, bingo_boards):
# an idea to play
# if a number on board - that number knocked out or converted to 999 say
# if an elemenet of list is all 999 - a row copleted
# a nested for loop can check if columns all 999
# if a solution found flag with board[1] set to true/ 1

	for index in range(0,len(bingo_numbers),5): # from given list select 5 numbers at a time
		numbers_to_call = [int(x) for x in bingo_numbers[index:index+5] ] #convert to int
		
		# using board[1] to test
		for board in range(0,100):
			for number in numbers_to_call:
				for row in range(2,7):
					for board_num in bingo_boards[board][row]:
						print(board, " ", row, ' ', number,' ', board_num, ' ', bingo_boards[board][row])
						if board_num == '': continue #a board contained extra '' - unable to see why so this skips it - clumsy but works...
						if number == int(board_num):
							print("Number: ",number, " in board row", bingo_boards[board][row])
							bingo_boards[board][row] = ['999' if x == board_num else x for x in bingo_boards[board][row]]
							print("Number: ",number, " in board ", bingo_boards[board][row])
							# check if a row is all '999'
							if bingo_boards[board][row] == ['999', '999', '999', '999', '999']:
								print("BINGO row!")
								return calulate_board_score(bingo_boards[board], number)

							#check if a column is all '999'
							for column in range(0,5):
								if (bingo_boards[board][2][column] == '999') and (bingo_boards[board][3][column] == '999') and (bingo_boards[board][4][column] == '999') and (bingo_boards[board][5][column] == '999') and (bingo_boards[board][6][column] == '999'):
									print('BINGO Column!')
									return calulate_board_score(bingo_boards[board], number)


	return

def calulate_board_score(complete_board, last_number_called):
	# find sum of non-999 values
	# multiply by last number called
	print(complete_board)
	print(last_number_called)
	sum = 0
	for row in range(2,7):
		for col in range(0,5):
			sum += (complete_board[row][col] == '999' * 0) + (complete_board[row][col] != '999') * int(complete_board[row][col])

	return sum * last_number_called

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d04-input.txt')
#split the given data in to game numbers drawn and boards
(numbers, boards) = split_data(input_data)
# play bingo
print("Part 1: Winning score is: ", play_bingo(numbers, boards))
print(numbers)