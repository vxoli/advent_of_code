f = open('d03-input.txt', 'r')
data = f.readlines()
trees = 0
col = 0
length = len(data[0])
for row in range(len(data)):
    if data[row][col] == "#":
            trees += 1 
    col = (col + 3) % (length-1)
print(trees)
