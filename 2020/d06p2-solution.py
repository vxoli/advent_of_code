import string

f = open('d06-input.txt', 'r')
data = f.readlines()
data_clean = []
lst = ""
count = 0
letter_count = 0
group = []
lttrs = []
for lines in data:
	group.append(lines)
	if lines == "\n":
		data_clean.append(group)
		group=[]
for i in data_clean:
	for letter in string.ascii_lowercase:
		letter_count = 0
		for j in range(0,len(i)-1):
			letter_count += i[j].count(letter)
			print(lines, i,i[j],letter,letter_count, count)
		if letter_count == len(i)-1:
			count += 1

		
#		for i in range(0,len(group)-1):
#			for idx, letter in enumerate(string.ascii_lowercase):
#				print(idx, letter, i, group[i])
#				if letter in group[i]:
#					lttrs[idx] += 1
#					print(lttrs[idx])
#				if letters[idx] == len(group)-1:
#					count += 1
#		group = []
#		lttrs = []
print(count)
# clean data string - get groups into one line each
#for lines in data:
#	if lines == "\n":
#		data_clean.append(lst.replace("\n", ""))
#		lst = ""
#		continue
#	else:
#		lst += lines
