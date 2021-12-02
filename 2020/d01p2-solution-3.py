f = open('d1p1-input.txt', 'r')
data = list(map(int, f.readlines()))

def loop():
	for x in data:
		for y in data:
			for z in data:
				if x + y + z == 2020: 
					print(x,y,z, x*y*z)
					return
loop()
