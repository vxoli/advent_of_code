import math
# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

# routine to rotate waypoint in E-N (x-y) plane
def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

#test data
#data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
# data = [list(line) for line in data]

directions = {"E","S","W","N"}
rotations = {"L","R"}

#dictionary of directions and set initial value
shipPosn = {"E":0 , "N":0} # W and S indicated by negative values
waypoint = {"E":10, "N":1} # W and S indicated by negative

for line in data:
	instruction = line[0]
	value = int(line[1:])
	if instruction == "F":
		shipPosn["N"] += waypoint["N"] * value
		shipPosn["E"] += waypoint["E"] * value
	if instruction in directions:
		if instruction in {"W", "S"}:
			value = -value
			if instruction == "W":
				instruction = "E"
			elif instruction == "S":
				instruction = "N"
		waypoint[instruction] += value
	if instruction in rotations:
		if instruction == "R":
			value = - value
		waypoint['E'], waypoint['N'] = rotate((0, 0), (waypoint['E'], waypoint['N']), math.radians(value))
	
distance = abs(shipPosn["E"]) + abs(shipPosn["N"])
print(f"Manhatten distance is: {distance}")
