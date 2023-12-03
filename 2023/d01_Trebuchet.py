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
  numberWords = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    'ten' : '10',
    'eleven' : '11',
    'twelve' : '12',
    'thirteen' : '13',
    'fourteen' : '14',
    'fifteen' : '15',
    'sixteen' : '16',
    'seventeen' : '17',
    'eighteen' : '18',
    'nineteen' : '19',
    'twenty' : '20'
  }
  result = ""
  currentWord = ""
  for char in string:
    if char.isalpha():
      currentWord += char
      for s in list(numberWords.keys()):
        if s in currentWord:
          result += numberWords.get(s.lower(), currentWord)
          currentWord = ""
    else:
      result += char
      currentWord = ""
    print(result)
  print(result)
  return str(result)

# Part 1

calibrationDocument = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d01_input.txt")
sum = 0
for line in calibrationDocument:
    digits = ''.join(c for c in line if c.isdigit())
    sum += int(digits[0]+digits[-1])

print("Part 1: Consider your entire calibration document. What is the sum of all of the calibration values?", sum)

# Part 2
""" calibrationDocument = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']
 """
sum = 0
for line in calibrationDocument:
    number = ""
    number = text2int(line)
    print(number,"|",number[0],"-",number[-1],"=", number[0]+number[-1])
    sum += int(number[0]+number[-1])
print(sum)