f = open('d01p1-input.txt', 'r')
data = list(map(int,f.readlines()))

def reconcile(x,y):
	if x + y == 2020: 
		print(x,y, x*y)
		return

[reconcile(x,y) for x in data for y in data]
