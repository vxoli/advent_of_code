# AoC 2022
# --- Day 21: Monkey Math ---

import urllib.request

def read_url(url): #read from github file
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def read_file(filename): # read from disk
	data = []
	with open(filename) as f:
		for line in f:
			data.append(line.strip())

	return data

def parse_input(data):
	data_dict = {}
	monkey_names = []
	for line in data:
		monkey_names.append(line.split(':')[0].strip())
		data_dict[line.split(':')[0]] = line.split(':')[1].strip()
	return monkey_names, data_dict

def part_1(monkey_names, input):
	while not input['root'].isnumeric():
		for monkey in monkey_names:
			if input[monkey].isnumeric(): continue
			if not input[monkey].isnumeric():
				first = input[monkey].split()[0].strip()
				last = input[monkey].split()[2].strip()
				operator = input[monkey].split()[1].strip()
				if input[first].isnumeric() and input[last].isnumeric():
					match operator:
						case '+':
							result = int(input[first]) + int(input[last])
						case '-':
							result = int(input[first]) - int(input[last])
						case '*':
							result = int(input[first]) * int(input[last])
						case '/':
							result = int(input[first]) // int(input[last])
					input_dict[monkey] = str(result)

	return input['root']

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d21-input.txt')
input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d21-input.txt")
input = ['root: pppw + sjmn','dbpl: 5','cczh: sllz + lgvd','zczc: 2','ptdq: humn - dvpt','dvpt: 3','lfqf: 4','humn: 5','ljgn: 2','sjmn: drzm * dbpl','sllz: 4','pppw: cczh / lfqf','lgvd: ljgn * ptdq','drzm: hmdt - zczc','hmdt: 32']

monkey_names, input_dict = parse_input(input)
print("Part 1: What number will the monkey named root yell?",part_1(monkey_names, input_dict))

