# Day 04: Scratchcards

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

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d04_input.txt")
data = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

numbers = [x.split(": ")[1].split(" | ") for x in data]

# loop through chosen numbers and check for winning numbers
score = 0
for number in numbers:
    count = 0
    myNumbers = number[1].split(" ") # split the string up
    myNumbers = [int(x.strip()) for x in myNumbers if x != ''] # re,move leading/ trailing whitespace and blank entries that occur
    winningNumbers = number[0].split(" ") # split the string up
    winningNumbers = [int(x.strip()) for x in winningNumbers if x != ''] # re,move leading/ trailing whitespace and blank entries that occur
    for num in myNumbers:
        if num in winningNumbers:
            count += 1
    score += int(pow(2, count-1) * (count > 0))
    print(score)
print("Take a seat in the large pile of colorful cards. How many points are they worth in total?",int(score))
        
        
