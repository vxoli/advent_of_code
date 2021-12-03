# oxygen_ratingoC 2021 D03

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines

def part1(report):
	
	# count the frequency of 1's in each position
	frequency = [0] * (len(report[1].strip('\n')))
	gamma = [0] * (len(report[1].strip('\n')))
	epsilon = [0]  * (len(report[1].strip('\n')))

	for line in report:
		for number in range(0,len(line)-1):
			frequency[number] += int(line[number])
			gamma[number] = int(frequency[number] > 500)
			epsilon[number] = int(not(gamma[number]))

	gamma_value = gamma[0]*2**11 + gamma[1]*2**10 + gamma[2]*2**9 + gamma[3]*2**8 + gamma[4]*2**7 + gamma[5] *2**6 + gamma[6]*2**5 + gamma[7]*2**4 + gamma[8]*2**3 + gamma[9]*2**2 + gamma[10]*2**1 + gamma[11]*2**0
	epislon_value = epsilon[0]*2**11 + epsilon[1]*2**10 + epsilon[2]*2**9 + epsilon[3]*2**8 + epsilon[4]*2**7 + epsilon[5] *2**6 + epsilon[6]*2**5 + epsilon[7]*2**4 + epsilon[8]*2**3 + epsilon[9]*2**2 + epsilon[10]*2**1 + epsilon[11]*2**0

	return gamma_value * epislon_value

def part2(report):
	oxygen_rating = report
	scrubber_rating = report
	for i in range(len(report[0])):
		if len(oxygen_rating) > 1:
			oxygen_rating0 = len([x for x in oxygen_rating if x[i] == '0'])
			oxygen_rating1 = len([x for x in oxygen_rating if x[i] == '1'])
			if oxygen_rating1 >= oxygen_rating0:
				oxygen_rating = [x for x in oxygen_rating if x[i] == '1']
			else:
				oxygen_rating = [x for x in oxygen_rating if x[i] == '0']
		if len(scrubber_rating) > 1:
			scrubber_rating0 = len([x for x in scrubber_rating if x[i] == '0'])
			scrubber_rating1 = len([x for x in scrubber_rating if x[i] == '1'])
			if scrubber_rating1 >= scrubber_rating0:
				scrubber_rating = [x for x in scrubber_rating if x[i] == '0']
			else:
				scrubber_rating = [x for x in scrubber_rating if x[i] == '1']

	return int(oxygen_rating[0],2) * int(scrubber_rating[0],2)




input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d03-input.txt')
print("Answer Part 1: ", part1(input_data))
print("Answer Part 2: ", part2(input_data))