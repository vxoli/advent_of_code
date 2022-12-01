# AoC 2022 D01
# Counting Calories

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines
def part_1(data):
    max_calories = 0
    calories = 0

    for line in input_data:
        if line != '\n':
            calories += int(line)
        if line == '\n':
            max_calories = ((max_calories > calories) * max_calories) + (max_calories <= calories) * calories
            calories = 0
    
    return max_calories

def part_2(data):
    max_calories = [0,1,2]
    calories = 0
    calorie_list = []

    for line in input_data:
        if line != '\n':
            calories += int(line)
        if line == '\n':
            calorie_list.append(calories)     
            calories = 0
    
    calorie_list.sort(reverse=True)
    return sum(calorie_list[:3])


#Read in data textfile
input_data = read_data('/home/christopher-spectre/Documents/code/adventofcode/2022/d01-input.txt')

# part one
print("Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? ", part_1(input_data))

# part two
print('Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?', part_2(input_data))