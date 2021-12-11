#Aoc 2021 d06

def read_input(filename):
	with open(filename) as file:
		lines = [lines.strip('\n') for lines in file]
		file.close()
	lines = [line.split(',') for line in lines]
	start_data = [int(x) for x in lines[0]]
	return lines

def part1(fish_data):
	number_fish = len(fish_data)
	for day in range(0,80):
		for index in range(0,len(fish_data)):
			timer = int(fish_data[index])
			timer += -1
			if timer == -1:
				timer = 6
				fish_data.append(8)
			fish_data[index] = timer

	return len(fish_data)

#main body
input_data = read_input('/home/christopher/Documents/GitHub/adventofcode/2021/d06-input.txt')[0]
print("Part 1: How many lanternfish would there be after 80 days? ", part1(input_data))