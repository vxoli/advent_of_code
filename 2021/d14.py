#AoC d14
#--- Day 14: Extended Polymerization ---
import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	template = data[0]
	rules = dict()
	for row in data[2:]:
		rules[row.split(" -> ")[0]] = row.split(" -> ")[1]
	return template, rules

def rule_match(pair, rules):
	return rules[pair]

def insert_element(pair, element):
	return pair[0] + element + pair[1]

def apply_rules(pairs, rules):
	for index,pair in enumerate(pairs):
		element = rule_match(pair, rules)
		template_pairs[index] = insert_element(pair, element)
	return ''.join(template_pairs)

def calculate_most_least(template):
	res = {}
	for keys in template:
		res[keys] = res.get(keys,0)+1
	max, min = 0,1000000000000000000
	for key in res:
		if res[key] > max: max = res[key]
		if res[key] < min: min = res[key]	

	return max - min

#main
template, rules = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d14-input.txt')
for i in range(10):
	template_pairs = [i + j for i,j in zip(template, template[1:])]
	template = apply_rules(template_pairs, rules)

print("Part 1: What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? ", calculate_most_least(template))