# AoC 2022
# --- Day 17: Pyroclastic Flow ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d17-input.txt')

input = ['>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'] # test input
ROCKS = [['####'],['.#.','###','.#.'],['..#','..#','###'],['#','#','#','#'],['##','##']]
WIDTH = 7
pile = ['+-------+']
[x,y] = [2,len(pile)+3]
shape = ROCKS[0]
width_shape = len(shape[0])
for move in input[0][0:5]:
	print(move)
	match move:
		case '>':
			if x + width_shape + 1 <= WIDTH:
				x += 1
		case '<':
			if x - 1 > 1:
				x -= 1
	print('x_start',x,'x_end',x+width_shape)
	y -= 1
	if y == 0:
		break
	print(x,y)