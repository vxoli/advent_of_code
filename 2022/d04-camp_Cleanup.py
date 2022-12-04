# AoC 2022
# --- Day 4: Camp Cleanup ---
import urllib.request
import string

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d04-input.txt')
