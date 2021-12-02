using DelimitedFiles
# Read data file
f = open("d03-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)
#Part 1
global trees = 0
global col = 1
global line_length = length(data[1])
for row in 1:length(data)
    if data[row][col] == '#'
        global trees += 1
    end
    global col = (col + 2) % (line_length)+1 # julia doesnt allow zero index - this calulates across 2 mod line_length then adds one to make total across 3
end
println("Part 1: Trees encountered= $trees")
# Part 2
trees =0 
col = 1
routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
answer = 0
for route in 1:length(routes)
    # reset variables fro the route
    global col = 1
    global trees = 0
    for row in 1:routes[route][2]:length(data)
        if data[row][col] == '#'
            global trees = trees + 1
        end
        global col = (col + routes[route][1]-1) % (line_length)+1
    end
    if answer != 0
        global answer = answer * trees
    else
        global answer = trees
    end
end
println("Part 2: Trees product= $answer")
