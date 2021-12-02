# read data file
f = open('d16-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
# Test data
# data = ["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50","your ticket:","7,1,14","","nearby tickets:","7,3,47","40,4,50","55,2,20","38,6,12"]

# Split data into areas - fields, my ticket, nearby tickets
fields, myTicket, nearbyTickets = {}, [], []
# split fields into dictionary with class type, min and max values
for idx, line in enumerate(data):
    if line == "": continue
    if line[:11] == "your ticket":
        break
    # split the line into text before the colon to form the key, then the value pairs afer the colon seperated by ' or ' to form value pairs
    fields[line.split(": ")[0]] = (line.split(": ")[1].split(" or ")[0], line.split(": ")[1].split(" or ")[1])
    #the min of the min value
    min_min = int(fields[line.split(": ")[0]][0].split("-")[0])
    # the max of the min value
    min_max = int(fields[line.split(": ")[0]][0].split("-")[1])
    #the min of the max value
    max_min = int(fields[line.split(": ")[0]][1].split("-")[0])
    #the max of the max value
    max_max = int(fields[line.split(": ")[0]][1].split("-")[1])
    # redefine the dictionary entry with new min/max values
    fields[line.split(": ")[0]] = (min_min, min_max, max_min, max_max)
# split myTicket data into list
for line in data[idx+1:]:
    if line == "": continue
    if line[:14] == "nearby tickets":
        break
    myTicket.append(line)
# split nearbyTicket data into list
for line in data[idx+4:]:
    if line == "": continue
    nearbyTickets.append(line)
# ignore my ticket
# loop though each field, and compare ticket values to given parameters
# store sum of invalid parameters
# can combine all parameters into one set to compare with each line of list
validParams = set() # define empty set
ticketScanningErrorRate = 0
# add paramteters to set as union of sets of values from fields
for keys in fields:
    validParams = validParams.union(set(range(fields[keys][0],fields[keys][1]+1)),set(range(fields[keys][2],fields[keys][3]+1)))
# loop though nearbyTickets and identify invalid tickets
inValid = set()
validTickets = set()
for ticket in nearbyTickets:
    values = ticket.split(",")
    for value in values:
        if not(int(value) in validParams):
            inValid.add(ticket)
# remove inValid tickets and generaate list of validTickets
validTickets = set(nearbyTickets).difference(inValid)

# got some help here:
# code below adapted from q-viper
# a dictionary to hold possible fields for each col
valid_tickets = list(validTickets)
possibleFields = {i: set(fields.keys()) for i in range(len(validTickets))}
for ticket in validTickets:
    for i, value in enumerate(ticket.split(",")):
        for keys in fields:
            #validParaams is intersection of set on lower-range values and set of upper-range values
            validParams = set(range(fields[keys][0],fields[keys][1]+1)) | set(range(fields[keys][2],fields[keys][3]+1))
            possible = False
            if int(value) in validParams:
                possible = True
            if not possible:
                possibleFields[i].discard(keys)
# remove repeated fields
## having problem with this segment of code - returns StopIteration error at line 73
## unable to trace source - something to do witht he way I've setup the lists???
## used code from https://github.com/q-viper/Adevent-Of-Code-2020/blob/master/Advent%20of%20code.ipynb
## and https://github.com/jakobsen/advent-of-code-2020/blob/master/16.py
## to help check and develop my code - still stuck here...
## answer calculated as 650080463519
for i in sorted(possibleFields, key=lambda k: len(possibleFields[k])):
    thisField = next(iter(possibleFields[i]))
    for j in possibleFields:
        if j != i:
            possibleFields[j].discard(thisField)
            
myTicket = [int(x) for x in lines[22].split(",")]
ans = 1
for i in possibleFields:
    if possibleFields[i].pop().startswith("departure"):
        ans *= myTicket[i]

print("Part 2:", ans)

