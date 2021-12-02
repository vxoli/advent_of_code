f = open('d03-input.txt', 'r')
data = f.readlines()
length = len(data[0])
routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
answer = 0
for route in range(len(routes)):
    col = 0
    trees = 0
    for row in range(0, len(data), routes[route][1]):
        if data[row][col] == "#":
                trees += 1
        col = (col + routes[route][0]) % (length-1)
    if answer != 0:
        answer = answer * trees
    else:
        answer = trees

print(answer)
