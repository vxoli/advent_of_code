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
	offset = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
	pixel_data = [["","",""],["","",""],["","",""]]

	for delta in offset:
		dx = delta[0]
		dy = delta[1]
		pixel = "."

		if (row + dx >= 0 and row + dx < rows) and (col + dy >= 0 and col + dy < cols):
			pixel = image_data[row+dx][col+dy]


		# print(row+dy,"--",col+dx,"-- ",image_data[row+dy][col+dx])
		pixel_data[dx+1][dy+1] = pixel

	return parse_to_binary( pixel_data[0]+pixel_data[1]+pixel_data[2])

def parse_to_binary(pixel_data):
	bin_str = ""
	for char in pixel_data:
		if char == ".": bin_str += "0"
		if char == "#": bin_str += "1"
	return int(bin_str, base=2)

def enhance_image(image_data, rows, cols):
	new_image = [["."]*(cols+1)]*(rows+1)
	for col in range(cols):
		for row in range(rows):
		# detect surrounding
			pixel_value = detect_pixels(row,col, image_data, rows, cols)
			image_enhancement_char = algorythm[pixel_value]
			new_image[row][col] = image_enhancement_char
	return new_image


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
# remember OutOfBound pixels = "." or 0

# have to adjust algorythm so image can grow and be infinite in size


new_image = enhance_image(enhance_image(image_data, rows, cols), rows, cols)
total = 0
for char in new_image:
	print(char)
