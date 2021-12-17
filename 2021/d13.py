# AoC 2021 d13
# --- Day 13: Transparent Origami ---

import urllib.request

def read_url():
	file = urllib.request.urlopen('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d13-input.txt')
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	folds = [x for x in data if x[:4] == "fold"]
	grid = data[:len(folds)]

	return grid,folds

# MAIN
grid_data, fold_data = read_url()
print(fold_data)