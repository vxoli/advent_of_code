using DelimitedFiles
f = open("d05-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)

# Part 1 - find highest seat id

global maxseatid=0
for line in data
    # split the ticketdata into row and seat info
    global row_code = line[1:7]
    global seat_code= line[8:end]
    global seatid = 0
    global seatrow = 0:127
    global seatnum = 0:7

    for s in row_code
        if s == 'F'
            global seatrow = seatrow[1:Integer(length(seatrow)/2)]
        else
            global seatrow = seatrow[Integer(length(seatrow)/2)+1:end]
        end
    end

    for s in seat_code
        if s == 'L'
            global seatnum = seatnum[1:Integer(length(seatnum)/2)]
        else
            global seatnum = seatnum[Integer(length(seatnum)/2)+1:end]
        end
        global seatid = seatrow[1] * 8 + seatnum[1]
        global maxseatid = (seatid * (seatid > maxseatid)) + (maxseatid * (seatid <= maxseatid))
    end
end
println("Part 1: Highest seat ID is: $maxseatid")

# Part 2
maxseatid=0
seatid=[]

for line in data
    global row_code = line[1:7]
    global seat_code= line[8:end]
    global seatrow = 0:127
	global seatnum = 0:7
	
    for s in row_code
        if s == 'F'
            seatrow = seatrow[1:Integer(length(seatrow)/2)]
        else
            seatrow = seatrow[Integer(length(seatrow)/2)+1:end]
		end
	end
    for s in seat_code
        if s == 'L'
            seatnum = seatnum[1:Integer(length(seatnum)/2)]
        else
            seatnum = seatnum[Integer(length(seatnum)/2)+1:end]
		end
	end
    push!(seatid, (seatrow[1] * 8 + seatnum[1]))
end

sort!(seatid)

for s in 1:length(seatid)-1
    if Integer(seatid[s+1] - seatid[s]) == 1
        continue
    else
        println("Part 2: seat id is: $(Integer((seatid[s+1]+seatid[s]) / 2))")
	end
end

