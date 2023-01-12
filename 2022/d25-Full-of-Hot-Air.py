# AoC 2022
# --- Day 25: Full of Hot Air ---
import urllib.request

def read_url(url): #read from github file
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def read_file(filename): # read from disk
	data = []
	with open(filename) as f:
		for line in f:
			data.append(line.strip())

	return data


def convert_snafu_to_decimal(snafu):
	decimal = 0
	for i,digit in enumerate(snafu):
		max_index = len(snafu)-1
		match digit:
			case '2': value = 2
			case '1': value = 1
			case '-': value = -1
			case '=': value = -2
			case '0': value = 0
		decimal += value * (5 ** (max_index - i))

	return decimal

def convert_decimal_to_snafu(decimal):
	# 4890 -> 2=-1=0
	# 4890 / 5 = 978 remainder 0
	# 972 / 5 = 195 remainder 3
	# 194 / 5 = 39 remainder 0
	# 38 / 5 = 7 remainder 4
	# 7 / 5 = 1 remainder 2
	# 1 / 5 = 0 remainder 1
	# base-5 -> 124030
	# snafu -> 2=-1=0
	
	snafu = []
	value = decimal
	while value > 0:
		value = value+2
		remainder = value % 5
		value = value // 5
		match remainder:
			case 0: snafu.insert(0, '=')
			case 1: snafu.insert(0,'-')
			case 2: snafu.insert(0,'0')
			case 3: snafu.insert(0,'1')
			case 4: snafu.insert(0,'2')

	return (''.join(snafu))

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d25-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d25-input.txt")
#input = ['1=-0-2','12111','2=0=','21','2=01','111','20012','112','1=-1=','1-12','12','1=','122'] # Test data
sum = 0
for digit in input:
	sum += convert_snafu_to_decimal(digit)
print("What SNAFU number do you supply to Bob's console?",convert_decimal_to_snafu(sum))