# AoC 2021 d16
# --- Day 16: Packet Decoder ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	# Test Data
	data[0]= 'D2FE28'
	return data[0]

def convert_hex_to_bin(hex_string):
	binary = ""
	for char in hex_string:
		binary += str(bin(int(char, 16))[2:].zfill(4))
	return binary

# MAIN
transmission_hex = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d16-input.txt')
transmission_bin = convert_hex_to_bin(transmission_hex)
print(transmission_bin)
