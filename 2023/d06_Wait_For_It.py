# --- Day 6: Wait For It ---

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
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d06_input.txt")
""" data = ['Time:      7  15   30',
'Distance:  9  40  200']
 """# By newtonian mechanics: s = ut + 1/2at^2
# t(race) = t(button) + t(moving)
# a=0 - constant speed once button released
# u = 1 x t(button) (increases 1mm.ms^-1)
# So: s = (t(button))(t(tmoving))
# And: t(race) = t(button) + t(moving)
# So - most useful form is:
# s = (t(button)).(t(race)-(t(button)))
# s = t(race).t(button) - t(button)^2
# s(max) when ds/dt = 0
# ds/dt(button) = t(race)-2t(button))

# Part 1
times = data[0].split(":")[1].strip().split(" ")
times = [int(x) for x in times if x !=""]
distances = data[1].split(":")[1].strip().split(" ")
distances = [int(x) for x in distances if x !=""]
print(times, distances)
score = 1
for counter, time in enumerate(times):
    sum = 0
    for duration in range(0,time,1):
        t_button = duration
        t_move = time - t_button
        s = t_button * time - pow(t_button,2)
        if s > distances[counter]: 
            sum += 1
    score = score * sum
print("Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?", score)