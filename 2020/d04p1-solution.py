f = open('d04-input.txt', 'r')
data = f.readlines()
data_str = ""
valid = 0
for lines in data:
	data_str += lines
data_str = data_str.split("\n\n")
for passport in data_str:
	if ("byr" in passport) and ("iyr" in passport) and ("eyr" in passport) and ("hgt" in passport) and ("hcl" in passport) and ("ecl" in passport) and ("pid" in passport):
		valid = valid + 1
print(valid)