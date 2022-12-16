# AoC 2022
# --- Day 15: Beacon Exclusion Zone ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def parse(input):
	co_ordinates = []
	SENSOR = 'S'
	BEACON = 'B'
	max_x = 0
	min_x = float('inf')
	max_y = 0
	min_y = 0
	for line in input:
		# s = sensor location, b = beacon location
		s = line.split(':')[0].split(',')
		s[0] = int(s[0].strip('Sensor at').strip('x='))
		s[1] = int(s[1].strip().strip('y='))
		b = line.split(':')[1].split(',')
		b[0] = int(b[0].strip('closest beacon is at').strip('x='))
		b[1] = int(b[1].strip().strip('y='))
		manhattan = abs((b[0]-s[0]) + (b[1]-s[1]))
		co_ordinates.append([s,b,manhattan])
	max_s_x = max([line[0][0] for line in co_ordinates])
	max_s_y = max([line[0][1] for line in co_ordinates])
	max_b_x = max([line[1][0] for line in co_ordinates])
	max_b_y = max([line[1][1] for line in co_ordinates])
	min_s_x = min([line[0][0] for line in co_ordinates])
	min_s_y = min([line[0][1] for line in co_ordinates])
	min_b_x = min([line[1][0] for line in co_ordinates])
	min_b_y = min([line[1][1] for line in co_ordinates])
	offsetx, offsety = min(min_s_x,min_b_x), min(min_s_y,min_b_y)
	
	return co_ordinates # return numerical x,y for Sensor and Beacon and manhattan distance

def part_1(co_ordinates):
	## Instead of forming grid and filling in - runs nto memory errors because grid is 4.5mill cols and 4.5 mill rows - run loop and calculate all the possible sites for each sensor - and then only record those that are in row 200000. !To Be Done!
	counter = 0
	posn = []
	for line in co_ordinates:
		sx = line[0][0]
		sy = line[0][1]
		bx = line[1][0]
		by = line[1][1]
		manhattan = line[2]
		print(sx,sy,bx,by,manhattan)
		# loop through all possible points manhattan dist from S
		for dist_x in range(manhattan+1):
			dist_y = manhattan-dist_x
			print(sx+dist_x,sy+dist_y)
			if sy+dist_y >= 10:
				if [sx+dist_x, sy+dist_y] not in posn:
					posn += [sx+dist_x,sy+dist_y]
					counter += 1
		print(counter)


	return

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d15-input.txt')
input = ['Sensor at x=2, y=18: closest beacon is at x=-2, y=15','Sensor at x=9, y=16: closest beacon is at x=10, y=16','Sensor at x=13, y=2: closest beacon is at x=15, y=3','Sensor at x=12, y=14: closest beacon is at x=10, y=16','Sensor at x=10, y=20: closest beacon is at x=10, y=16','Sensor at x=14, y=17: closest beacon is at x=10, y=16','Sensor at x=8, y=7: closest beacon is at x=2, y=10','Sensor at x=2, y=0: closest beacon is at x=2, y=10','Sensor at x=0, y=11: closest beacon is at x=2, y=10','Sensor at x=20, y=14: closest beacon is at x=25, y=17','Sensor at x=17, y=20: closest beacon is at x=21, y=22','Sensor at x=16, y=7: closest beacon is at x=15, y=3','Sensor at x=14, y=3: closest beacon is at x=15, y=3','Sensor at x=20, y=1: closest beacon is at x=15, y=3']

co_ordinates = parse(input)
part_1(co_ordinates)

