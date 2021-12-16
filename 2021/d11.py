#Aoc 2021 d11
#--- Day 11: Dumbo Octopus ---

def read_file(filename):
	with open(filename) as file:
		data = file.read().strip()
	return data

def part1(octopus_map):
	octopus_map = ["11111","19991","19191","19991","11111"]
	new_octopus_map = []
	flashes = 0
	for row_index,row in enumerate(octopus_map):
		new_octopus_map.append("")
		for col_index,col in enumerate(row):
			energy_level = int(col)
			energy_level += 1
			if energy_level > 9: #Octopus flashes and gives 1 energy to all 8 adjacent octopuses
				flashes += 1
				energy_level = 0
				# update energy level of adjecent octopuses
				for ajdacent in {(-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1,-1), (1,0), (1,1)}:
					# if OOB continue
					if row_index + ajdacent[0] < 0: continue
					if col_index + ajdacent[1] < 0: continue
					if row_index + ajdacent[0] > len(octopus_map): continue
					if col_index + ajdacent[1] > len(row): continue
					octopus_map[row_index+ajdacent[0]] = octopus_map[row_index+ajdacent[0]][:col_index+ajdacent[1]] + str(int(octopus_map[row_index+ajdacent[0]][col_index+ajdacent[0]])+1) + octopus_map[row_index+ajdacent[0]][col_index+ajdacent[1]+1:]
					if octopus_map[row_index+ajdacent[0]][col_index]					

			new_octopus_map[row_index] = new_octopus_map[row_index] + str(energy_level)
	octopus_map = new_octopus_map
	print(octopus_map)

	return

#main
input_data = read_file("/home/christopher/Documents/GitHub/adventofcode/2021/d11-input.txt")
part1(input_data)