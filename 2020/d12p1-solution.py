# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
# data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
# data = [list(line) for line in data]

directions = {"E","S","W","N"}
rotations = {"L","R"}
current_posn = {"E":0, "S":0, "W":0, "N":0}
#dictionary of direction and current value
# set starting facing direction to east
# 90 degrees = E, 180 = S, 270 = W, 0/360 = N
compass = 90 

for line in data:
    instruction = line[0]
    value = int(line[1:])
    if instruction == "F":
        if compass == 0:
            current_posn["N"] += value
        if compass == 90:
            current_posn["E"] += value
        if compass == 180:
            current_posn["S"] += value
        if compass == 270:
            current_posn["W"] += value
    if instruction in directions:
        current_posn[instruction] += value
    if instruction in rotations:
        if instruction == "R":
            compass += value
            compass = compass % 360
        if instruction == "L":
            compass -= value
            compass = compass % 360
    
distance = (current_posn["E"]-current_posn["W"]) + (current_posn["S"]- current_posn["N"]) 
print(f"Manhatten distance is: {distance}")
