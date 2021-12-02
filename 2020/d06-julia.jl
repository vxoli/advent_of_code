readInput() = split.(split(read("d06-input.txt", String), "\n\n"))
data = readInput()

# solve by creating a set of responses.
# Part 1 : answers for anyone is the union of sets of answers
# Part 2 : answers for everyone in the intersection of the sets of answers

global part1 = 0
global part2 = 0
for line in data
    if line == [] continue end
    txt1 = ""
    txt2 = line[1]
	for x in 1:length(line)
        txt1 = ∪(txt1,line[x]) # ∪ symbol for union
        txt2 = ∩(txt2, line[x]) # ∩ symbol for intersection
	end
    global part1 += length(txt1)
    global part2 += length(txt2)
end
println("Part 1: the number of questions to which anyone answered \"yes\" = : $part1")
println("Part 2: the number of questions to which everyone answered \"yes\" = : $part2")
