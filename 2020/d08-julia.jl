# read data file
readInput() = split(read("d08-input.txt", String), "\n")
data = readInput()
# test data
# data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]

# Part 1

# initialise variables
global codeLine = 1
global accumulator = 0
global executedCodeLines = []
global repeatedLines = false

# loop until a line is repeated
while !(repeatedLines)
    # split input data into components
    command = data[codeLine][1:3]
    value = parse(Int64, data[codeLine][5:end])
    # if the line of code has been executed then change the repeatedLines variable
    if codeLine in executedCodeLines
        global repeatedLines = true
        break
    else push!(executedCodeLines, codeLine)
    end
    # execute the commands
    if command == "acc"
        global accumulator += value
        global codeLine += 1
    end
    if command == "nop"
        codeLine += 1
    end
    if command == "jmp"
        codeLine += value
    end
end
# print result
println("Immediately before any instruction is executed a second time, what value is in the accumulator?")
println(accumulator)

# Part 2

# identify all the lines with jmp or nop
testLines = []
for (idx, i) in enumerate(data)
    if (i[1:3] == "jmp") | (i[1:3] == "nop")
        push!(testLines, idx-1) # ?? should this -1 be here - trying to convert betwwen python 0 index and julia 1 index.
	end
end

# loop through the list changing each in turn to the other

for idx in testLines
    if data[idx][1:3] == "jmp"
		data[idx] = replace(data[idx], "jmp" => "nop")
    else
        data[idx] = replace(data[idx], "nop" => "jmp")
	end

# initialise variables
    global codeLine = 1
    global accumulator = 0
    global executedCodeLines = []
    global lastJmpLine = []
    global repeatedLines = false

    # while-loop until a line is repeated
    while !(repeatedLines)
        # split input data into components
        command = data[codeLine][1:3]
        value = parse(Int64, data[codeLine][5:end])
        # if the line of code has been executed then change the repeatedLines variable
        if codeLine in executedCodeLines
            global repeatedLines = true
            # reset the change code line then end the loop
            if data[idx][1:3] == "jmp"
                data[idx] = replace(data[idx], "jmp" => "nop")
            else
                data[idx] = replace(data[idx], "nop" => "jmp")
            end
            break
        else push!(executedCodeLines, codeLine)
		end
        # execute the commands
        if command == "acc"
            global accumulator += value
            global codeLine += 1
		end
        if command == "nop"
            codeLine += 1
		end
        if command == "jmp"
            codeLine += value
		end
        if codeLine > length(data)
            break
		end
    end # while
    if (repeatedLines == false) & (codeLine == length(data))
        break
	end
end # for idx

println(accumulator)
