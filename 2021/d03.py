# AoC 2021 D03

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines

def part1(report):
	
	# count the frequency of 1's in each position
	frequency = [0,0,0,0,0,0,0,0,0,0,0,0]
	gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
	epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

	for line in report:
		for number in range(0,len(line)-1):
			frequency[number] += int(line[number])
		gamma[0] = int(frequency[0] > 500)
		epsilon[0] = int(not(gamma[0]))
		gamma[1] = int(frequency[1] > 500)
		epsilon[1] = int(not(gamma[1]))
		gamma[2] = int(frequency[2] > 500)
		epsilon[2] = int(not(gamma[2]))
		gamma[3] = int(frequency[3] > 500)
		epsilon[3] = int(not(gamma[3]))
		gamma[4] = int(frequency[4] > 500)
		epsilon[4] = int(not(gamma[4]))
		gamma[5] = int(frequency[5] > 500)
		epsilon[5] = int(not(gamma[5]))
		gamma[6] = int(frequency[6] > 500)
		epsilon[6] = int(not(gamma[6]))
		gamma[7] = int(frequency[7] > 500)
		epsilon[7] = int(not(gamma[7]))
		gamma[8] = int(frequency[8] > 500)
		epsilon[8] = int(not(gamma[8]))
		gamma[9] = int(frequency[9] > 500)
		epsilon[9] = int(not(gamma[9]))
		gamma[10] = int(frequency[10] > 500)
		epsilon[10] = int(not(gamma[10]))
		gamma[11] = int(frequency[11] > 500)
		epsilon[11] = int(not(gamma[11]))
	
		gamma_value = gamma[0]*2**11 + gamma[1]*2**10 + gamma[2]*2**9 + gamma[3]*2**8 + gamma[4]*2**7 + gamma[5] *2**6 + gamma[6]*2**5 + gamma[7]*2**4 + gamma[8]*2**3 + gamma[9]*2**2 + gamma[10]*2**1 + gamma[11]*2**0
		epislon_value = epsilon[0]*2**11 + epsilon[1]*2**10 + epsilon[2]*2**9 + epsilon[3]*2**8 + epsilon[4]*2**7 + epsilon[5] *2**6 + epsilon[6]*2**5 + epsilon[7]*2**4 + epsilon[8]*2**3 + epsilon[9]*2**2 + epsilon[10]*2**1 + epsilon[11]*2**0

	print(gamma, "--", gamma_value)
	print(epsilon, "--", epislon_value)

	return gamma_value * epislon_value


input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d03-input.txt')
print("Answer Part 1: ", part1(input_data))