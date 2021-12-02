using DelimitedFiles
f = open("d01p1-input.txt")
data = readdlm(f, '\t', Int, '\n')
close(f)
println("Part 1:")
for x in data
	for y in data
		if (x + y) == 2020
            println(x, "\t", y, "\t",(x*y))
        end
    end
end
println("Part2:")
for x in data
	for y in data
        for z in data
        	if (x + y + z) == 2020
                println(x, "\t", y, "\t", z,"\t",(x*y*z))
            end
        end
    end
end
