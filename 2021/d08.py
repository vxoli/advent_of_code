#Aoc 2021 d08

def read_data(filename):
	with open(filename) as file:
		data = file.readlines()

	return data

def part1(codes):
	# loop through all codes in list
	# split line at |
	# 1 has 2 codes, 4 uses 4 codes, 7 uses 3 codes, 8 uses all 7 codes.
	# count the number of times a 2/4/3 or 7 letter code appears
	# return answer
	counter = 0
	for line in codes:
		output_code = line.split('|')[1]
		for each_code in output_code.split(' '):
			if len(each_code.strip()) in {2,4,3,7}:
				counter += 1
	return counter

def part2(inputs):	# bit of copying here from the web: inter alia
					# https://zonito.medium.com/seven-segment-search-day-8-advent-of-code-2021-21e5bc965005
					# https://andreyorst.gitlab.io/posts/2021-12-08-advent-of-code-day-8/
					# https://blog.cristiana.tech/advent-of-code-2021-day-8
					
	outputs = list(map(format, [input.split('|')[1].strip().split() for input in inputs]))
	inputs = list(map(format, [input.split('|')[0].strip().split() for input in inputs]))

	code = []
	mapping = {2: 1, 3: 7, 4: 4, 7: 8}
	for input in inputs:
	    temp = {}
	    for word in input:
	        if len(word) in mapping:
	            temp[mapping[len(word)]] = word
	    
	    # Find 6
	    for word in input:
	        if len(word) == 6 and any(char not in word for char in temp[1]):
	            temp[6] = word
	            break# Find 0
	    for word in input:
	        if len(word) == 6 and any(char not in word for char in temp[4]) and word not in temp.values():
	            temp[0] = word
	            break
	    
	    # Find 9 after 6 and 0 with length 6
	    for word in input:
	        if len(word) == 6 and word not in temp.values():
	            temp[9] = word
	            break# Find 5
	    for word in input:
	        if len(word) == 5 and all(char in temp[6] for char in word):
	            temp[5] = word
	            break
	    
	    # Find 3
	    for word in input:
	        if len(word) == 5 and all(char in temp[9] for char in word) and word not in temp.values():
	            temp[3] = word
	            break
	    
	    # Find 2 after 3 and 5 with length 5
	    for word in input:
	        if len(word) == 5 and word not in temp.values():
	            temp[2] = word
	    
	    # Transform key-value to value-key
	    code.append({v: k for k, v in temp.items()})
	total = 0
	for i, output in enumerate(outputs):
	    total += int(''.join(map(str, [code[i][word] for word in output])))

	return total

def format(input):
    return list(map(lambda w: ''.join(sorted(w)), input))


#main
input_data = read_data("/home/christopher/Documents/GitHub/adventofcode/2021/d08-input.txt")
print("Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear? ", part1(input_data))
print("Part 2: What do you get if you add up all of the output values? ",part2(input_data))