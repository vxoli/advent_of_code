f = open('d07-input.txt', 'r')
data = f.readlines()
# data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.", "dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "bright white bags contain 1 shiny gold bag." , "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags." , "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags." , "dark olive bags contain 3 faded blue bags, 4 dotted black bags.", "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags." , "faded blue bags contain no other bags.", "dotted black bags contain no other bags."]
myBags = []
data_clean = [data[i].split("contain") for i in range(len(data))]
print(data_clean[1][0])
print(data_clean[1][1])
# find the bags that can contain "shiny gold bags"
myBags = [data_clean[s][0][0:len(data_clean[s][0])-6] for s in range(len(data_clean)) if "shiny gold" in data_clean[s][1]]

# find bags that can contain bags that can contain "shiny gold bags"
for bag_col in myBags:
	myBags += [data_clean[s][0][0:len(data_clean[s][0])-6] for s in range(len(data_clean)) if bag_col in data_clean[s][1]]

# remove duplicate bag colours
myBags = list(dict.fromkeys(myBags))
print(myBags)
print(len(myBags))
