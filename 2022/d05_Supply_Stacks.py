#AoC 2022
# --- Day 05: Supply Stacks ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

data = read_url(url)
