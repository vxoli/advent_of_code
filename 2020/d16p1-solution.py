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
    for idx in range(0,len(fields[keys])-1,2):
        validParams = validParams | set(range(fields[keys][idx],fields[keys][idx+1]+1))
# loop though nearbyTickets and sum values not in parameters
for line in nearbyTickets:
    values = line.split(",")
    for value in values:
        ticketScanningErrorRate += int(not(int(value) in validParams)) * int(value)
print("ticket scanning error rate =",ticketScanningErrorRate)