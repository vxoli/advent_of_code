f = open('d01p1-input.txt', 'r')
data = f.readlines()
data = list(map(int,data))
for x in data:
	for y in data:
		for z in data:
			if x + y + z == 2020: 
				print(x,y,z, x*y*z)
				break
