# read data file
f = open('d13-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
# Test data
# data = ["939","7,13,x,x,59,x,31,19"]

# splice timestamp from data
timestamp = int(data[0])
# split buscodes at ',' and remove 'x' and convert to integers
buscodes = ["x" if line == "x" else int(line) for line in data[1].split(",")]

mods = {bus: -i % bus for i, bus in enumerate(buscodes) if bus != "x"}
times = list(reversed(sorted(mods)))
timestamp = mods[times[0]]
r = times[0]
for b in times[1:]:
	while timestamp % b != mods[b]:
		timestamp += r
	r *= b

print(f"answer = {timestamp}")