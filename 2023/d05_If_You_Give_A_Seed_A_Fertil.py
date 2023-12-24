# --- Day 5: If You Give A Seed A Fertilizer ---

import urllib.request

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    return data

## MAIN
## Part 1
almanac = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d05_input.txt")
almanac = ['seeds: 79 14 55 13',
'',
'seed-to-soil map:',
'50 98 2',
'52 50 48',
'',
'soil-to-fertilizer map:',
'0 15 37',
'37 52 2',
'39 0 15',
'',
'fertilizer-to-water map:',
'49 53 8',
'0 11 42',
'42 0 7',
'57 7 4',
'',
'water-to-light map:',
'88 18 7',
'18 25 70',
'',
'light-to-temperature map:',
'45 77 23',
'81 45 19',
'68 64 13',
'',
'temperature-to-humidity map:',
'0 69 1',
'1 0 69',
'',
'humidity-to-location map:',
'60 56 37',
'56 93 4']

# data wrangling to split into sections from almanacsections by the headings
# use the headings as dict keys and store the values in lists
mapType = ""
sections = dict()
for row in almanac:
    if row[0:6]=="seeds:":
        mapType = "seeds"
        sections[mapType] = row.split(":")[1].strip().split(" ")
        
    if row == '': continue
    if row[0].isalpha():
        mapType = row.strip(":")
        continue
    if row[0].isdigit():
        if mapType in sections.keys():
            sections[mapType].append(row.split(" "))
        else:
            sections[mapType] = [row.split(" ")]

    