# AoC 2021 d22
# --- Day 22: Reactor Reboot ---
import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")

	return data
