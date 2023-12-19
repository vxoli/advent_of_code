# --- Day 16: The Floor Will Be Lava ---

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

# MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d16_input.txt")
data = ['.|...\....',
'|.-.\.....',
'.....|-...',
'........|.',
'..........',
'.........\ ',
'..../.\\..',
'.-.-/..|..',
'.|....-|.\ ',
'..//.|....']
print(data)