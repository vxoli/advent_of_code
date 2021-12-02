f = open('d02-input.txt', 'r')
data = f.readlines()
data = [x.strip().split() for x in data]
valid = 0
for row in range(len(data)):
	# min value = data[row][0].split('-')[0]
	# max value = data[row][0].split('-')[1]
	# character = data[row][1].split(':')[0]
	# password to test = data[row][2]
	# number occurances of letter = data[row][2].count(data[row][1].split(':')[0])
	max = int(data[row][0].split('-')[1])
	min = int(data[row][0].split('-')[0])
	char_count = data[row][2].count(data[row][1].split(':')[0])
	valid += (char_count >= min) * (char_count <= max)
print(valid)