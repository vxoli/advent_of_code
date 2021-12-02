# read data file
f = open('d09-input.txt', 'r')
data = f.readlines()
# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing
for i in range(0,len(data)):
    data[i] = int(data[i].strip("\n"))
# print(data[preamble:])

for idx, i in enumerate(data[preamble:]):
    solution = False
    # print("idx",idx,"i",i)
    for j in data[idx:idx+preamble]:
        for k in data[idx:idx+preamble]:
            if j + k == i and (j != k):
                # print("i",i,"j",j,"k",k)
                solution = True
                break
        if solution == True:
            break
    if solution == False:
        break
# i is the value, data.index(i) is the position of i in the list
# need to loop through the data list to the position of i to find
# a combination of two or more numbers that sum to i
targetNumber = i
targetIdx = data.index(i)

for i in range(0,targetIdx):
    sum = 0
    values = []
    for j in data[i:targetIdx]:
        if i == j:
            continue
        sum += j
        values.append(j)
        if sum == targetNumber:
            print(targetNumber, sum, values)
            print(min(values) + max(values))
            break
        if sum > targetNumber:
            break
