# AoC 2022
# --- Day 22: Monkey Map ---
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


#input = read_url('https://raw.githubusercontent.com/vxoli/advent_of_code/main/2022/d22-input.txt')
input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d22-input.txt")

#input =['         ...#','        .#..','        #...','       ....','...#.......#','........#...','..#....#....','..........#.','        ...#....','        .....#..','        .#......','        ......#.','','10R5L5R10L4R5L5']

board = []
for i in input[:-1]:
	if i == '': continue
	board.append(i.strip())
path = input[-1]

# parse path
idx = 0
commands = []
curr_num = ""
for idx in range(len(path)):
	if path[idx].isdigit():
		curr_num += path[idx]
	else:
		commands.append(int(curr_num))
		curr_num = ""
		commands.append(path[idx])

# if last command is a number
if curr_num != "":
	commands.append(int(curr_num))

dirs = [[0,1],[1,0],[0,-1],[-1,0]]

# parse the board
nrows = len(board)
ncols = max([len(row) for row in board])

bound_row = [[ncols, -1] for _ in range(nrows)]
bound_col = [[ncols, -1] for _ in range(ncols)]

adj = set()
for row, line in enumerate(board):
	for col in range(len(line)):
		c = line[col]
		if c == ".":
			adj.add((row,col))
		if c in ['.','#']:
			bound_row[row][0] = min(bound_row[row][0], col)
			bound_row[row][1] = max(bound_row[row][1], col)
			bound_col[col][0] = min(bound_col[col][0], row)
			bound_col[col][1] = max(bound_col[col][1], row)

# Follow the instructions
direction = 0
row = 0
col = bound_row[0][0]

for cmd in commands:
	if isinstance(cmd, str):
		if cmd == 'L':
			direction = (direction -1) % 4
		else:
			direction = (direction + 1) % 4
		continue

	drow, dcol = dirs[direction]

	for _ in range(cmd):
		if (row,col) not in adj:
			break
		new_row = row + drow
		new_col = col + dcol

		if drow != 0:
			rbounds = bound_col[col]
			height = rbounds[1] - rbounds[0] +1
			new_row = (new_row - rbounds[0]) % height + rbounds[0]

		if dcol != 0:
			cbounds = bound_row[row]
			width = cbounds[1] -cbounds[0] + 1
			new_col = (new_col - cbounds[0]) % width + cbounds[0]

		if (new_row, new_col) not in adj:
			break

		row,col = new_row, new_col

ans = 1000* (row+1) +4*(col+1) + direction
print("Part 1: Follow the path given in the monkeys' notes. What is the final password?",ans)
