f = open('d02-input.txt', 'r')
data = f.readlines()
data = [x.strip().split() for x in data]
valid = 0
for row in range(len(data)):
	# char_pos_1 = data[row][0].split('-')[0]
	# char_pos_2 = data[row][0].split('-')[1]
	# character = data[row][1].split(':')[0]
	# password to test = data[row][2]
	# number occurances of letter = data[row][2].count(data[row][1].split(':')[0])
	test_char = data[row][1].split(':')[0]
	char_pos_2 = int(data[row][0].split('-')[1]) - 1
	char_pos_1 = int(data[row][0].split('-')[0]) - 1
	# valid =+ (data[row][2][char_pos_1] == test_char) * (data[row][2][char_pos_2] == test_char)
	if (data[row][2][char_pos_1] == test_char and data[row][2][char_pos_2] != test_char) or (data[row][2][char_pos_1] != test_char and data[row][2][char_pos_2] == test_char):
		valid = valid + 1
print(valid)