# AoC 2021 d10
#--- Day 10: Syntax Scoring ---

def read_file(filename):
	with open(filename) as file:
		data = [x for x in file.read().strip().split('\n')]
	file.close()
	return data

def part1(chunks):
# chunks = ["[({(<(())[]>[[{[]{<()<>>",
# "[(()[<>])]({[<{<<[]>>(",
# "{([(<{}[<>[]}>{[]{[(<()>",
# "(((({<>}<{<{<>}{[]{[]{}",
# "[[<[([]))<([[{}[[()]]]",
# "[{[{({}]{}}([{[{{{}}([]",
# "{<[[]]>}<{[{[{[]{()[[[]",
# "[<(<(<(<{}))><([]([]()",
# "<{([([[(<>()){}]>(<<{{",
# "<{([{{}}[<[[[<>{}]]]>[]]"]

	brackets = ["()","[]","{}","<>"]
	scores = {
			")": 3,
			"]": 57,
			"}":1197,
			">":25137}
	syntax_error_score = 0
	stack = []

	for line in chunks:
		for char in line:
			if char == '\n': continue
			good = False
			for bracket in brackets:
				if char == bracket[0]:
					stack.append(char)
					good = True
				elif char == bracket[1]:
					if stack[-1] == bracket[0]:
						stack.pop()
						good=True
			if not good:
				syntax_error_score += scores[char]
				break

	return syntax_error_score

def part2(chunks):
	brackets = ["()","[]","{}","<>"]
	stack = []
	good_lines = []

	# find good lines
	for line in chunks:
		for char in line:
			if char == '\n': continue
			good = False
			for bracket in brackets:
				if char == bracket[0]:
					stack.append(char)
					good = True
				elif char == bracket[1]:
					if stack[-1] == bracket[0]:
						stack.pop()
						good=True
		if good:
			good_lines.append(line)

	# use stack to complete lines
	stack = []
	added = []
	autocomplete_score = 0
	autocomplete_scores = []
	scores = {
			")":1,
			"]":2,
			"}":3,
			">":4}

	for line in good_lines:
		added = []
		autocomplete_score = 0
		for char in line:
			if char == "\n": continue
			for bracket in brackets:
				if char == bracket[0]:
					stack.append(char)
				if char == bracket[1]:
					if stack[-1] == bracket[0]:
						stack.pop()
					else:
						added.append(bracket[1])
						
		for c in added:
			autocomplete_score *= 5
			autocomplete_score += scores[c]
		autocomplete_scores.append(autocomplete_score)


	sorted_scores = list(set(autocomplete_scores))
	sorted_scores.sort()
	print(sorted_scores)
	return sorted_scores[int((len(sorted_scores)-2)/2)]

## main
input_data = read_file("/home/christopher/Documents/GitHub/adventofcode/2021/d10-input.txt")
print("Part 1: What is the total syntax error score for those errors? ", part1(input_data))
print("Part 2: What is the middle score? ",part2(input_data))