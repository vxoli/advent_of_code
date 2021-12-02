# read data file
f = open('d08-input.txt', 'r')
data = f.readlines()
# test data
# data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]

# initialise variables
codeLine = 0
accumulator = 0
executedCodeLines = []
repeatedLines = False

# loop until a line is repeated
while not(repeatedLines):
    # split input data into components
    command = data[codeLine][0:3]
    value = data[codeLine][3:]
    # if the line of code has been executed then change the repeatedLines variable
    if codeLine in executedCodeLines:
        repeatedLines = True
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

# print result
print(accumulator)
