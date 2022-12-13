#Aoc @022
# --- Day 11: Monkey in the Middle ---

import urllib.request
import string

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def split_input(data):
	d = {}
	for c, chunk in enumerate(data):
		if chunk.startswith("Monkey"):
			d[chunk.strip(':')] = [data[c+1].strip(), data[c+2].strip(), data[c+3].strip(), data[c+4].strip(), data[c+5].strip()]
	
	for monkey in d.copy():
		d[monkey][0] = d[monkey][0].strip("Starting items: ").split(",")
		d[monkey[0]] = [int(i) for i in d[monkey][0]]
		d[monkey][1] = d[monkey][1].strip("Operation: new")
		d[monkey][2] = int(d[monkey][2].strip('Test: divisible by'))
		d[monkey][3] = int(d[monkey][3].strip('If true: throw to monkey'))
		d[monkey][4] = int(d[monkey][4].strip('If false: throw to monkey'))
		d[monkey].append(0)
	del d['M']
	return d

def monkey_throws(data, part):
	for m, monkey in enumerate(data.copy()):
		# calculate worry level
		starting_items = data[monkey][0]
		operation = data[monkey][1].split()
		decision = data[monkey][2]
		monkey_to_true = data[monkey][3]
		monkey_to_false = data[monkey][4]
		for worry in starting_items.copy():
			data[monkey][5] += 1
			if operation[1] == 'old' and operation[3] == 'old':
				value = int(worry)
			else: value = int(operation[3])
			match operation[2]:
				case '*':
					worry_level = int(worry) * value
				case '+':
					worry_level = int(worry) + value
			# now relax and divide by three, round down.
			if part == 1: worry_level = (worry_level // 3)

			# deciode what to do with item
			if (worry_level % decision) == 0: # if decision true
			 	to_monkey = 'Monkey '+ str(monkey_to_true)
			 	data[to_monkey][0].append(str(worry_level))
			 	data[monkey][0].remove(str(worry))
			else: 
			 	to_monkey = 'Monkey '+str(monkey_to_false)
			 	data[to_monkey][0].append(str(worry_level))
			 	data[monkey][0].remove(str(worry))
				
	return data

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d11-input.txt')
#input = ['Monkey 0:','  Starting items: 79, 98','  Operation: new = old * 19','  Test: divisible by 23','    If true: throw to monkey 2','    If false: throw to monkey 3','', 'Monkey 1:','  Starting items: 54, 65, 75, 74','  Operation: new = old + 6','  Test: divisible by 19','    If true: throw to monkey 2','    If false: throw to monkey 0','','Monkey 2:','  Starting items: 79, 60, 97','  Operation: new = old * old','  Test: divisible by 13','    If true: throw to monkey 1','    If false: throw to monkey 3','', 'Monkey 3:','  Starting items: 74','  Operation: new = old + 3','  Test: divisible by 17','    If true: throw to monkey 0','    If false: throw to monkey 1']
input = split_input(input)
for i in range(20):
	input = monkey_throws(input, 1)
total = []
for i, monkey in enumerate(input):
	total.append(input[monkey][5])
total.sort()
print('Part 1: What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?',total[-2:][0] * total[-2:][1])
for i in range(10000):
	print(i)
	input = monkey_throws(input,2)
total = []
for i, monkey in enumerate(input):
	total.append(input[monkey][5])
total.sort()
print('Part 2: What is the level of monkey business after 10000 rounds of stuff-slinging simian shenanigans?',total[-2:][0] * total[-2:][1])