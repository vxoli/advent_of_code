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

#main
template, rules = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d14-input.txt')
for i in range(10):
	template_pairs = [i + j for i,j in zip(template, template[1:])]
	template = apply_rules(template_pairs, rules)
