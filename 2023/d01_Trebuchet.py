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

calibrationDocument = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d01_input.txt")
sum = 0
for line in calibrationDocument:
    digits = ''.join(c for c in line if c.isdigit())
    number = digits[0]+digits[-1]
    sum += int(number)

print("Consider your entire calibration document. What is the sum of all of the calibration values?", sum)
    