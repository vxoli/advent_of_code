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

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d11-input.txt')
input = ['Monkey 0:','  Starting items: 79, 98','  Operation: new = old * 19','  Test: divisible by 23','    If true: throw to monkey 2','    If false: throw to monkey 3','', 'Monkey 1:','  Starting items: 54, 65, 75, 74','  Operation: new = old + 6','  Test: divisible by 19','    If true: throw to monkey 2','    If false: throw to monkey 0','','Monkey 2:','  Starting items: 79, 60, 97','  Operation: new = old * old','  Test: divisible by 13','    If true: throw to monkey 1','    If false: throw to monkey 3','', 'Monkey 3:','  Starting items: 74','  Operation: new = old + 3','  Test: divisible by 17','    If true: throw to monkey 0','    If false: throw to monkey 1']
print(split_input(input))