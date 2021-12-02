# given data set of starting numbers
data = [0,5,4,1,10,14,7]

# test data
# data = [0,3,6]

spokenNumbers = {} #{i:0 for i in data}
turn = 0
spoken= data[0]

# loop through starting numbers
for idx, number in enumerate(data):
	turn += 1
	spoken = number
	# if in the dictionary, the difference in turns since last spoken becomes new spoken and update the turn spoken in dictionary
	if spoken in spokenNumbers.keys():
		spokenNumbers[spoken]=turn - spokenNumbers[spoken]
	if not(spoken in spokenNumbers.keys()):
		spokenNumbers[spoken]=turn
		spoken = 0

# loop to target value
while turn < 2020:
	turn += 1
	if turn == 2020: print(turn, spoken)

	# if in the dictionary, the difference in turns since last spoken becomes new spoken and update the turn spoken in dictionary
	if spoken in spokenNumbers.keys():
		nextspoken = turn - spokenNumbers[spoken]
		spokenNumbers[spoken]=turn

	else:
		spokenNumbers[spoken]=turn
		nextspoken=0
	spoken = nextspoken


	