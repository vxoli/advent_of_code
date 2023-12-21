# --- Day 19: Aplenty ---

import urllib.request

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    """ data = ['px{a<2006:qkq,m>2090:A,rfg}','pv{a>1716:R,A}','lnx{m>1548:A,A}','rfg{s<537:gd,x>2440:R,A}','qs{s>3448:A,lnx}','qkq{x<1416:A,crn}','crn{x>2662:A,R}','in{s<1351:px,qqz}','qqz{s>2770:qs,m<1801:hdj,R}','gd{a>3333:R,R}','hdj{m>838:A,pv}',
            '',
            '{x=787,m=2655,a=1222,s=2876}','{x=1679,m=44,a=2067,s=496}','{x=2036,m=264,a=79,s=2244}','{x=2461,m=1339,a=466,s=291}','{x=2127,m=1623,a=2188,s=1013}'] """
    # find the blank row then split the data set into workflows and part ratings
    blankRow = [int(r) for r,row in enumerate(data) if row == ""]
    blankRow = int(blankRow[0])
    workFlows = data[:blankRow]
    partRatings = data[blankRow+1:]
    # convert workFlows into a set of {workflowName: conditions}
    workFlows = {row.split('{')[0]: row.split('{')[1].strip('}').split(',') for row in workFlows}
    # strip { and } from lines of partRatings
    partRatings = [row.strip('{}') for row in partRatings]
        
    return workFlows,partRatings


# MAIN
workFlows, partRatings = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d19_input.txt")
total = 0
for rating in partRatings:
    action = ''
    flow = 'in' # all workFlows start with flow called 'in'
    # select the starting conditions
    i = 0
    while action not in ['A','R']:
        conditions = workFlows[flow]
    # loop through the list of conditions
    # there may be an unconditional branch with no condition - need to deal with that
        condition = conditions[i] # THIS NEEDS TO BECOME A WHILE LOOP SO CONDITIONS CAN BE RESET
        if ':' not in condition: # these are the unconditional branches or A or R
            if condition in ['A','R']:
                action = condition
                break
            else:
                flow = condition # the condition will contain the flow name to branch to -> update the flow
                i=0
        else:
            # seperate the condition into the parameter to check, the symbol < or > and the value
            test = condition.split(':')[0]
            action = condition.split(':')[1]
            if '<' in test:
                symbol = '<'
                parameter, specification = test.split('<')
            if '>' in test:
                symbol = '>'
                parameter, specification = test.split('>')
            # convert the ratings to dictionary to make selecting the parameter easier
            ratings = {r.split('=')[0]: r.split('=')[1] for r in rating.split(',')}
            # now select the parameter from the partRatings and compare to the required value
            value = ratings[parameter]

            # perform the comparison and return the result
            if symbol == '<':
                if int(value) < int(specification): 
                    flow = action
                    i=0
                else: 
                    i += 1
                    action = ""
            if symbol == '>':
                if int(value) > int(specification): 
                    flow = action
                    i=0
                else: 
                    i += 1
                    action = ""
            
    if action == 'A':
        total += sum([int(v) for v in ratings.values()])

print("Part 1: What do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?",total)                
                