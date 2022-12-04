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

def part_1(data):
    counter = 0 
    # In how many assignment pairs does one range fully contain the other?
    for pair in data:
        elf1_assigned = ""
        elf2_assigned = ""
        elf1,elf2 = pair.split(',')
        elf1_start,elf1_end = elf1.split('-')
        elf2_start,elf2_end = elf2.split('-')

        #generate list of assigned area IDs
        for i in range(int(elf1_start),int(elf1_end)+1):
            elf1_assigned += str(i)+'-'
        for i in range(int(elf2_start), int(elf2_end)+1):
            elf2_assigned += str(i)+'-'
        elf1_assigned, elf2_assigned = elf1_assigned[:-1], elf2_assigned[:-1]
        print(elf1,"   ",elf2)
        print(elf1_assigned,"\n",elf2_assigned)
        print((elf1_assigned in elf2_assigned) or (elf2_assigned in elf1_assigned))

        # check if one assigned list contained within the other
        #if (elf1_assigned in elf2_assigned) or (elf2_assigned in elf1_assigned):
        #    counter += 1
        counter += (elf1_assigned in elf2_assigned) + (elf2_assigned in elf1_assigned)

    return counter

data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d04-input.txt')
print(part_1(data))