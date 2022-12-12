#Aoc @022
# --- Day 11: Monkey in the Middle ---

import urllib.request

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
	return d

def part_1(data):
	for m, monkey in enumerate(data):
	# calculate worry level
		starting_items = data[monkey][0].strip("Starting items: ").split(",")
		starting_items = [int(i) for i in starting_items]
		operation = data[monkey][1].strip("Operation: new =old").split()
		decision = int(data[monkey][2].strip('Test: divisible by'))
		monkey_to_true = int(data[monkey][3].strip('If true: throw to monkey'))
		monkey_to_false = int(data[monkey][4].strip('If false: throw to monkey'))
		for worry in starting_items:
			if len(operation) == 2:
				value = int(operation[1])
			else: value = int(worry)
			match operation[0]:
				case '*':
					worry_level = worry * value
				case '+':
					worry_level = worry + value
			# now relax and divide by three, round down.
			worry_level = (worry_level // 3)
			print(worry_level)

			# deciode what to do with item
			if (worry_level % decision) == 0:
				print(data[monkey][3],'---',data[monkey][3][-1])	
			else: print(data[monkey][4],'---',data[monkey][4][-1])

	return

# input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d11-input.txt')
input = ['Monkey 0:','  Starting items: 79, 98','  Operation: new = old * 19','  Test: divisible by 23','    If true: throw to monkey 2','    If false: throw to monkey 3','', 'Monkey 1:','  Starting items: 54, 65, 75, 74','  Operation: new = old + 6','  Test: divisible by 19','    If true: throw to monkey 2','    If false: throw to monkey 0','','Monkey 2:','  Starting items: 79, 60, 97','  Operation: new = old * old','  Test: divisible by 13','    If true: throw to monkey 1','    If false: throw to monkey 3','', 'Monkey 3:','  Starting items: 74','  Operation: new = old + 3','  Test: divisible by 17','    If true: throw to monkey 0','    If false: throw to monkey 1']
input = split_input(input)
print(part_1(input))