# read data file
f = open('d08-input.txt', 'r')
data = f.readlines()
# test data
# data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]


# TRY:
# identify all the lines with jmp or nop
# loop through the list changing each in turn to the other
# if code executes - flag success
# if code repeats revert data set and swop next matching command and try again

# identify all the lines with jmp or nop
testLines = []
for idx, i in enumerate(data):
    if i[0:3] == "jmp" or i[0:3] == "nop":
        testLines.append(idx)
# loop through the list changing each in turn to the other

for idx in testLines:
    if data[idx][0:3] == "jmp":
        data[idx] = data[idx].replace("jmp","nop")
    else:
        data[idx] = data[idx].replace("nop", "jmp")
    
    # initialise variables
    codeLine = 0
    accumulator = 0
    executedCodeLines = []
    lastJmpLine = []
    repeatedLines = False
    
    # while-loop until a line is repeated
    while not(repeatedLines):
        # split input data into components
        command = data[codeLine][0:3]
        value = data[codeLine][3:]
        # if the line of code has been executed then change the repeatedLines variable
        if codeLine in executedCodeLines:
            repeatedLines = True
            # reset the change code line then end the loop
            if data[idx][0:3] == "jmp":
                data[idx] = data[idx].replace("jmp","nop")
            else:
                data[idx] = data[idx].replace("nop", "jmp")
            break
        else: executedCodeLines.append(codeLine)
        # executed the commands
        if command == "acc":
            accumulator += int(value)
            codeLine += 1
        if command == "nop":
            codeLine += 1
        if command == "jmp":
            codeLine += int(value)
        if codeLine > len(data)-1:
            break
    if (repeatedLines == False) and (codeLine == len(data)):
        break

print(accumulator)