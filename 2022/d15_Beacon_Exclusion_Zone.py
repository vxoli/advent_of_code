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
	co_ordinates = set()
	SENSOR = 'S'
	BEACON = 'B'
	max_x = 0
	min_x = float('inf')
	max_y = 0
	min_y = 0
	for line in input:
		# s = sensor location, b = beacon location
		s = line.split(':')[0].split(',')
		s0 = int(s[0].strip('Sensor at').strip('x='))
		s1 = int(s[1].strip().strip('y='))
		b = line.split(':')[1].split(',')
		b0 = int(b[0].strip('closest beacon is at').strip('x='))
		b1 = int(b[1].strip().strip('y='))
		manhattan = abs(b0-s0) + abs(b1-s1)
		co_ordinates.add(('S',s0,s1,'B',b0,b1,manhattan))

	# max_s_x = max([line[1] for line in co_ordinates])
	# max_s_y = max([line[2] for line in co_ordinates])
	# max_b_x = max([line[4] for line in co_ordinates])
	# max_b_y = max([line[5] for line in co_ordinates])
	# min_s_x = min([line[1] for line in co_ordinates])
	# min_s_y = min([line[2] for line in co_ordinates])
	# min_b_x = min([line[4] for line in co_ordinates])
	# min_b_y = min([line[5] for line in co_ordinates])
	# offsetx, offsety = min(min_s_x,min_b_x), min(min_s_y,min_b_y)
	
	return co_ordinates # return numerical x,y for Sensor and Beacon and manhattan distance

def part_1(co_ordinates):
	## Instead of forming grid and filling in - runs nto memory errors because grid is 4.5mill cols and 4.5 mill rows - run loop and calculate all the possible sites for each sensor - store in set, and then return those that are in row 200000.
	counter = 0
	beacon_posn = set([(i[4],i[5]) for i in co_ordinates])
	sensor_posn = set([(i[1],i[2]) for i in co_ordinates])
	no_beacon_posn = set()
	for line in co_ordinates:
		sx = line[1]
		sy = line[2]
		bx = line[4]
		by = line[5]
		manhattan = line[6]
		# loop through all possible points manhattan dist from S and store coords in no_beacons
		for i in range(manhattan+1):
			for j in range(manhattan-i+1):
				if (sy+ j == 10) or (sy -j == 10): 
					no_beacon_posn.add((sx+i,sy+j))
					no_beacon_posn.add((sx+i,sy-j))
					no_beacon_posn.add((sx-i,sy+j))
					no_beacon_posn.add((sx-i,sy-j))

	return len([i for i in no_beacon_posn.difference(beacon_posn, sensor_posn) if i[1]==10])

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d15-input.txt')
input = [	'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
			'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
			'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
			'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
			'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
			'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
			'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
			'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
			'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
			'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
			'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
			'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
			'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
			'Sensor at x=20, y=1: closest beacon is at x=15, y=3']

co_ordinates = parse(input)
print(part_1(co_ordinates))

