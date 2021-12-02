f = open('d01p1-input.txt', 'r')
data = f.readlines()
data = list(map(int,data))
for x in data:
	for y in data:
		if x + y == 2020: print(x,y, x*y)
