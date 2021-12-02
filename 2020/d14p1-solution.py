# read data file
f = open('d14-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
# Test data
# data = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","mem[8] = 11","mem[7] = 101", "mem[8] = 0"]

# define dictionary to store memory addresses
memoryAddresses = []
# loop though data and if new memoryadress add to list
for line in data:
    if line[:4] == "mem[":
        #splice the memory address and value from string
        memAddr = int(line[line.index("[")+1:line.index("]")])
        if memAddr in memoryAddresses:
            continue
        else:
            memoryAddresses.append(memAddr)
# use list of memory addresses to define dictionary
memory = {i:0 for i in memoryAddresses}

for line in data:
    if line[:4] == "mask":
        bitmask = line[7:]
# convert decimal to 36 bit binary: print(format(32, '#038b').replace("0b",""))
    if line[:4] == "mem[":
        #splice the memory address and value from string
        memAddr = int(line[line.index("[")+1:line.index("]")])
        value = line[line.index("=")+2:]
        # convert value to 36 bit binary (bin adds 0b to end - once removed 38 length number becomes 36)
        valueBin = format(int(value), '#038b').replace("0b","")
        newValueBin = ""
        # apply bitmask to valueBin to produce newValueBin
        for idx,digit in enumerate(bitmask):
            if digit == "X":
                newValueBin += valueBin[idx]
            if digit == "1":
                newValueBin += "1"
            if digit == "0":
                newValueBin += "0"
        # store newValueBin in memory slot memAddr
        memory[memAddr] = int(newValueBin,2)
# sum all non-zero value in memory{}
total = 0
for i in memory:
    if memory[i] >0:
        total += memory[i]
print(f"sum of values = {total}")
