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

def text2int(string):

  for word, number in numberWords.items():
    string = string.replace(str(number), word)
  return string
    
def find_substrings_with_digits(string):
  substrings_with_indicies = []
  for word in numberWords:
    index = string.find(word)
    while index != -1:
      substrings_with_indicies.append((word, index))
      index = string.find(word, index+1)
  substrings_with_indicies.sort(key=lambda x:x[1])
  substrings_translated = [numberWords[word] for word,_ in substrings_with_indicies]
  return substrings_translated

# Part 1

calibrationDocument = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d01_input.txt")
""" calibrationDocument = ['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet'] """
sum = 0
for line in calibrationDocument:
    digits = ''.join(c for c in line if c.isdigit())
    sum += int(digits[0]+digits[-1])

print("Part 1: Consider your entire calibration document. What is the sum of all of the calibration values?", sum)

# Part 2
# tried converting words to numbers - didn't work - too complicated.
# now trying converting numbers to words then back again...
# need to accont for lines with only single digit.
numberWords = {
  'zero' : 0,
  'one' : 1,
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9
}
""" calibrationDocument = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen'] """
sum = 0
for line in calibrationDocument:
  numbersInWords = text2int(line)
  substrings = find_substrings_with_digits(numbersInWords)
  first = substrings[0]
  last = substrings[-1]
  final_digit = first*10 + last
  sum += final_digit
  
print("Part 2: What is the sum of all of the calibration values?", sum)

# thoughts on previous solution - would have worked but had too many numbers in words. sixteen should covert to 6 not 16 for the puzzle to work.
