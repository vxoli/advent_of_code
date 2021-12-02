f = open('d01p1-input.txt', 'r')
data = list(map(int,f.readlines()))

def loop():
	for x in data:
		for y in data:
			if x + y == 2020: 
				print(x,y, x*y)
				return
loop()
