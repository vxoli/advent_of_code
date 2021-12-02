f = open("d04-input.txt", "r")
data = read(f, String)
close(f)
# clean data
# need to strip the double '\n\n' indicates new passport data - strip from the dataset
data = split(data, "\n\n")
# replace remaining eol (\n) chars in string with spaces
for i in 1:length(data)
    global data[i] = replace(data[i], "\n" => " ")
end

validpart1 = 0
validpart2 = 0
for (index, passport) in enumerate(data)
    # the following test check for valid passports in part 1, and is first test for part 2
    if occursin("byr", passport) & occursin("iyr", passport) & occursin("eyr", passport) & occursin("hgt", passport) & occursin("hcl", passport) & occursin("ecl", passport) & occursin("pid", passport)
        global validpart1 = validpart1 + 1

        # start of checks for part 2
        # determine birth year byr
        byr = parse(Int, split(split(split(passport, "byr")[2], ":")[2], " ")[1])
        # determine issue year iyr
        iyr = parse(Int, split(split(split(passport, "iyr")[2], ":")[2], " ")[1])
        # determine expiration year eyr 
        eyr = parse(Int, split(split(split(passport, "eyr")[2], ":")[2], " ")[1])
        # determine height hgt & units
        hgt_length = length(split(split(split(passport, "hgt")[2], ":")[2], " ")[1])
        # check units included
        hgt_unit = split(split(split(passport, "hgt")[2], ":")[2], " ")[1][hgt_length-1:hgt_length]
        if !occursin(r"cm|in", hgt_unit) continue end
        hgt = parse(Int, split(split(split(passport, "hgt")[2], ":")[2], " ")[1][1:hgt_length-2])
        # determine hair colour hcl
        hcl = split(split(split(passport, "hcl")[2], ":")[2], " ")[1]
        # determine eye colour ecl
        ecl = split(split(split(passport, "ecl")[2], ":")[2], " ")[1]
        # determine passport id pid
        pid = split(split(split(passport, "pid")[2], ":")[2], " ")[1]
        # ignore cid

        # check if parameters in range
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        # cid (Country ID) - ignored, missing or not.
        if ((byr >= 1920) & (byr <= 2002)) & 
            ((iyr >= 2010 & iyr <= 2020)) & 
            ((eyr >= 2020) & (eyr <= 2030)) & 
            occursin(r"^#[0-9A-Fa-f]{6}$", hcl) & 
            occursin(r"amb|blu|brn|gry|grn|hzl|oth", ecl) & 
            occursin(r"\d{9}", pid) & 
            (((hgt_unit == "cm") & (hgt >= 150) & (hgt <= 193)) | ((hgt_unit == "in") & (hgt >=59) & (hgt <= 76)))
            global validpart2 = validpart2 + 1
        end # if ((byr >= ....))

    end #if occursin
end #for passport in data

println("Part 1: Valid passports = $validpart1")
println("Part 2: Valid passports = $validpart2")

