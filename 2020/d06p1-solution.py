import string
f = open('d06-input.txt', 'r')
data = f.readlines()
data_clean = []
lst = ""
count = 0
# clean data string - get groups into one line each
for lines in data:
	if lines == "\n":
		data_clean.append(lst.replace("\n", ""))
		lst = ""
		continue
	else:
		lst += lines

#loop through each line
for lines in data_clean:
# loop through a...z
	for letter in string.ascii_lowercase:
# if that letter in the line increment counter
		if letter in lines:
			count += 1
print(count)
