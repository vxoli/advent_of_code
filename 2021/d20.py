# AoC 2021 d20
# --- Day 20: Trench Map ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	algorythm = data[0]
	image_data = data[2:]
	return algorythm, image_data

def detect_pixels(row,col,image_data, rows, cols):
	offset = [(-1,-1),(0,-1),(1,-1),(0,-1),(0,0),(0,1),(-1,1),(0,1),(1,1)]
	pixel_data = [[".",".","."],[".",".","."],[".",".","."]]

	for delta in offset:
		print(delta)
		dx = delta[0]
		dy = delta[1]
		pixel = "."

		if (row + dx >= 0 and row + dx < rows) and (col + dy >= 0 and col + dy < cols):
			pixel = image_data[row+dx][col+dy]


		# print(row+dy,"--",col+dx,"-- ",image_data[row+dy][col+dx])
		pixel_data[dx+1][dy+1] = pixel
	print(pixel_data)
	return #pixel_data


# MAIN
algorythm, image_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d20-input.txt')
#TEST DATA
image_data = ['#..#.','#....','##..#','..#..','..###']

rows = len(image_data)
cols = len(image_data[0])

# loop through each dot
# detect surrounding cells
# determine binary number
# apply algorythm
# generate new image with result
# remember oob pixels = "." or 0


for col in range(cols):
	for row in range(rows):
# detect surrounding
		pixel_map = detect_pixels(row,col, image_data, rows, cols)