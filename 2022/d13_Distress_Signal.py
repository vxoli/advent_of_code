# AoC 2022
# --- Day 13: Distress Signal  ---

import urllib.request
import ast
from functools import cmp_to_key, reduce
import operator

def read_url(url):
	f = urllib.request.urlopen(url)
	data = f.read()
	data = data.decode('utf8')
	data = [[ast.literal_eval(line) for line in pair.strip().split("\n")] for pair in data.split("\n\n")]

	return data

def cmp_values(left: int | list, right: int | list) -> int:
    match left, right:
        case int(), int():
            return (left < right) - (left > right)
        case list(), list():
            for cmp_val in map(cmp_values, left, right):
                if cmp_val:
                    return cmp_val
            return cmp_values(len(left), len(right))
        case int(), list():
            return cmp_values([left], right)
        case list(), int():
            return cmp_values(left, [right])
    raise ValueError(f"Invalid types: {type(left)} and {type(right)}")


def part_1(data):

	return sum([ind for ind, line in enumerate(input, 1) if cmp_values(*line) == 1])

def part_2(data):
	keys = [[[2]], [[6]]]
	flat_lines = keys + [item for sublist in data for item in sublist]
	flat_lines.sort(key=cmp_to_key(cmp_values), reverse=True)

	return reduce(operator.mul, [ind for ind, x in enumerate(flat_lines, 1) if x in keys])


input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d13-input.txt')
print(input)
print("Part 1: What is the sum of the indices of those pairs?",part_1(input))
print(part_2(input))