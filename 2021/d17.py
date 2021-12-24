# Aoc 2021 d17
# --- Day 17: Trick Shot ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	data = data[0][len("target area: x="):]
	data = data.split(", y=")

	x_range = (int(data[0][:data[0].index("..")]),
		int(data[0][data[0].index("..")+2:]) )
	y_range = (int(data[1][:data[1].index("..")]),
		int(data[1][data[1].index("..")+2:]) )

	return (x_range, y_range)

def steps_for_dy(dy):
    y = 0
    steps = 0
    valid = []
    while y >= miny:
        if miny <= y <= maxy:
            valid.append(steps)
        y += dy
        dy -= 1
        steps += 1
    return valid

def hit_target(step):
	for dx in range(1, maxx):
		x = 0
		for _ in step:
		    x += dx
		    if dx > 0:
		        dx -= 1
		if minx <= x <= maxx:
		    return True
	return False


# MAIN
target = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d17-input.txt')
minx = target[0][0]
maxx = target[0][1]
miny = target[1][0]
maxy = target[1][1]
dy = abs(miny)

def part1(dy):
	while True:
		steps = steps_for_dy(dy)
		if dy < -100: break
		if hit_target(steps): break
		dy -= 1
	return sum(range(1,dy+1))


# set of points in the range
start=(0,0)
target_area = set()
for x in range(target[0][0],target[0][1]):
	for y in range(target[1][0],target[1][1]):
		target_area.add((x,y))
posn = (0,0)


print("What is the highest y position it reaches on this trajectory? ",part1(dy))




## ??Useful?? formulae:
## (n) + (n-1) + (n-2) + (n-3) ... (n-k) = n+ nk-k(k+1)/2
##										= n + nk - (k^2)/2 - k/2
##										= n + (n-1/2)k - (k^2)/2
## roots = (-b +-sqr(b^2-4ac))/2a

