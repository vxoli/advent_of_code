# read data file
f = open('d13-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
# Test data
# data = ["939","7,13,x,x,59,x,31,19"]

# splice timestamp from data
timestamp = int(data[0])
# split buscodes at ',' and remove 'x' and convert to integers
buscodes = [int(line) for line in data[1].split(",") if line != "x"]

noBus = True
time = timestamp - 1
while noBus:
	time += 1	
	for bus in buscodes:
		if time % bus == 0:
			noBus = False
			break
			
print(f"earliest departure time: {time}, delay: {time-timestamp}min, catch bus: {bus}")
print(f"answer = {bus * (time-timestamp)}")