# Day 1: Trebuchet

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = 0
    result = ""
    for word in textnum.split():
        if word not in numwords:
          increment = word
        else:
            scale, increment = numwords[word]
        result = result + str(increment)
        
    return result

# Part 1

calibrationDocument = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d01_input.txt")
sum = 0
for line in calibrationDocument:
    digits = ''.join(c for c in line if c.isdigit())
    sum += int(digits[0]+digits[-1])

print("Part 1: Consider your entire calibration document. What is the sum of all of the calibration values?", sum)

# Part 2
numberWords = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sum = 0
for line in calibrationDocument:
    number = ""
    for numberWord in numberWords:
        if numberWord in line:
            number = number + " " + numberWord
    num = text2int(number)
    print(num,num[0],num[-1], num[0]+num[-1])
    sum += int(num[0]+num[-1])
print(sum)