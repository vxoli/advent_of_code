# AoC 2021 d16
# --- Day 16: Packet Decoder ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	return

# MAIN
input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d15-input.txt')