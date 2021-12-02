f = open('d1p1-input.txt', 'r')
data = list(map(int,f.readlines()))

def reconcile(x,y,z):
	if x + y + z == 2020: 
		print(x,y,z, x*y*z)
		return

[reconcile(x,y,z) for x in data for y in data for z in data]
