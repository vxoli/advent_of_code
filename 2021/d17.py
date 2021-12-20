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


# MAIN
target = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d17-input.txt')
print(target)