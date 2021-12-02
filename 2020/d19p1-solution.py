# read data file
with open("d19-input.txt") as f:
    raw_rules, message = f.read().split('\n\n')
    raw_rules = raw_rules.splitlines()
    message = message.splitlines()
	
# Test data