# AoC 2021 d22
# --- Day 22: Reactor Reboot ---
import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")

	return data

def parse_data(input):
	operator = line[0]
	xyz = line[1].split(",")
	x_min = int(xyz[0].split("..")[0][2:])
	x_max = int(xyz[0].split("..")[1])
	y_min = int(xyz[1].split("..")[0][2:])
	y_max = int(xyz[1].split("..")[1])
	z_min = int(xyz[2].split("..")[0][2:])
	z_max = int(xyz[2].split("..")[1])

	return (operator, x_min, x_max, y_min, y_max, z_min, z_max)

# Main
data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d22-input.txt')

part1_data = []
for x in data:
	temp = x.split()
	xyz = temp[1].split(",")
	if -50 <= int(xyz[0].split("..")[0][2:]) <= 50 and -50 <= int(xyz[0].split("..")[1]) <= 50 and -50 <= int(xyz[1].split("..")[0][2:]) <= 50 and -50 <= int(xyz[1].split("..")[1]) <= 50 and -50 <= int(xyz[2].split("..")[0][2:]) <= 50 and -50 <= int(xyz[2].split("..")[1]) <= 50:
		part1_data.append(temp)

cubes_on = set()
for line in part1_data:
	cubes = set()
	operator, x_min, x_max, y_min, y_max, z_min, z_max = parse_data(line)
	for x in range(x_min,x_max):
		for y in range(y_min,y_max):
			for z in range(z_min,z_max):
				cubes.add((x,y,z))
	if operator == "on":
		#union sets cubes_on and cubes
		cubes_on = cubes_on.union(cubes)
	if operator == "off":
		# intersection sets cubes_on and cubes
		cubes_on = cubes_on.difference(cubes)

print(cubes_on)
