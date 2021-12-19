# Aoc 2021 d15
# --- Day 15: Chiton ---
import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	#data = data.split("\n")
	data = [[int(i) for i in line] for line in data.split("\n")]
	
	return data


# Main
map_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d15-input.txt')
print(map_data)