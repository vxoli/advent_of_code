# read data file
readInput() = split(read("d09-input.txt", String), "\n")
stringData = readInput()
# convert strings to Integer
data = []
for i in stringData
    push!(data, parse(Int,i))
end

# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing

#Part 1

for (idx,i) in enumerate(data[preamble+1:end])
    global solution = false
    # println("idx",idx," i",i)
    for j in data[idx:idx+preamble-1]
        for k in data[idx:idx+preamble-1]
            if (j + k == i) &&  (j != k)
                # println("i",i,"j",j,"k",k)
                global solution = true
                break
            end
        end
        if solution == true
            break
        end
    end
    if solution == false
        println("The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property? ",i)
        return global targetNumber = i
        break
    end
end

# Part 2

# i is the value, indexin(i, data) is the position of i in the list
# need to loop through the data list to the position of i to find 
# a combination of two or more numbers that sum to i
#global targetNumber = i
global targetIdx = indexin(targetNumber, data)[1]
for i in 1:targetIdx-1
    sum = 0
    vals = []
    for j in data[i:targetIdx]
        if i == j
            continue
        end
        sum += j
        push!(vals, j)
        if sum == targetNumber
            # println(targetNumber, " ", sum, " ", vals)
            println("What is the encryption weakness in your XMAS-encrypted list of numbers? ", minimum(vals) + maximum(vals))
            break
        end
        if sum > targetNumber
            break
        end
    end
end



