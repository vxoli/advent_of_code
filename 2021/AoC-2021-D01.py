# AoC 2021 D1

# AoC 2021 D1

with open('/Users/mummydaddy/OneDrive/Documents/GitHub/D01-input.txt') as f:
	lines = f.readlines()
	f.close()

for line in lines:
	if line < line.next():
		counter += 1
print(counter)
