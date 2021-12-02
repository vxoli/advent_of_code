using System;
using System.Collections.Generic;
using System.IO;

namespace c__d08
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines(@"../d08-input.txt");
            //PART 1
            //initialise variables
            int accumulator = 0, codeLine=0;
            var executedCodeLines = new List<int>();
            bool repeatedLines = false;

            //loop until a line is repeated
            while (!repeatedLines)
            {
                //split data into components
                var command = data[codeLine].Split(" ")[0];
                var value = data[codeLine].Split(" ")[1];
                if (executedCodeLines.Contains(codeLine)) 
                {
                    repeatedLines = true;
                    break;                    
                }
                else
                {   //update the list of executed commands
                    executedCodeLines.Add(codeLine);
                    //execute the commands
                    if (command == "acc") {accumulator += int.Parse(value); codeLine++;}
                    if (command == "nop") codeLine++;
                    if (command == "jmp") codeLine += int.Parse(value);
                }
            }
            Console.WriteLine("Part 1: Immediately before any instruction is executed a second time, what value is in the accumulator? {0}", accumulator);
            
            //PART 2
            //identify all the lines with jmp or nop
            var testLines = new List<int>();
            codeLine = 0;
            foreach (var line in data)
            {
                var command = data[codeLine].Split(" ")[0];
                var value = data[codeLine].Split(" ")[1];
                if ((command == "jmp") | (command == "nop")) testLines.Add(codeLine);
                codeLine++;
            }
            //loop through the list changing each in turn to the other
            codeLine = 0;
            foreach (var index in testLines)
            {
                var command = data[index].Split(" ")[0];
                var value = data[index].Split(" ")[1];
                if (command == "jmp") data[index].Replace("jmp", "nop");
                else data[index].Replace("nop","jmp");                
            
                //initialise variables
                codeLine = 0;
                accumulator = 0;
                executedCodeLines.Clear();
                var lastJmpLine = new List<int>();
                repeatedLines = false;
            
                //while-loop until a line is repeated
                while (!repeatedLines)
                {
                    command = data[codeLine].Split(" ")[0];
                    value = data[codeLine].Split(" ")[1];
                    //if the line of code has been executed then change the repeatedLines variable
                    if (executedCodeLines.Contains(codeLine))
                    {
                        repeatedLines = true;
                        //reset the change code line then end the loop
                        if (command == "jmp") data[index] = data[index].Replace("jmp","nop");
                        else data[index] = data[index].Replace("nop","jmp");
                        break;
                    }
                    else executedCodeLines.Add(codeLine);
                    
                    //execute the commands
                    if (command == "acc")
                    {
                        accumulator += int.Parse(value);
                        codeLine++;
                    }
                    if (command == "nop") codeLine++;
                    if (command == "jmp") codeLine += int.Parse(value);
                    if (codeLine > data.Length-1) break;
                }
            if ((repeatedLines == false) && (codeLine == data.Length)) break;
        }
        Console.WriteLine(accumulator);
        }
    }
}

/* # read data file
f = open('d08-input.txt', 'r')
data = f.readlines()
# test data
# data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]


# TRY:
# identify all the lines with jmp or nop
# loop through the list changing each in turn to the other
# if code executes - flag success
# if code repeats revert data set and swop next matching command and try again

# identify all the lines with jmp or nop
testLines = []
for idx, i in enumerate(data):
    if i[0:3] == "jmp" or i[0:3] == "nop":
        testLines.append(idx)
# loop through the list changing each in turn to the other

for idx in testLines:
    if data[idx][0:3] == "jmp":
        data[idx] = data[idx].replace("jmp","nop")
    else:
        data[idx] = data[idx].replace("nop", "jmp")
    
    # initialise variables
    codeLine = 0
    accumulator = 0
    executedCodeLines = []
    lastJmpLine = []
    repeatedLines = False
    
    # while-loop until a line is repeated
    while not(repeatedLines):
        # split input data into components
        command = data[codeLine][0:3]
        value = data[codeLine][3:]
        # if the line of code has been executed then change the repeatedLines variable
        if codeLine in executedCodeLines:
            repeatedLines = True
            # reset the change code line then end the loop
            if data[idx][0:3] == "jmp":
                data[idx] = data[idx].replace("jmp","nop")
            else:
                data[idx] = data[idx].replace("nop", "jmp")
            break
        else: executedCodeLines.append(codeLine)
        # executed the commands
        if command == "acc":
            accumulator += int(value)
            codeLine += 1
        if command == "nop":
            codeLine += 1
        if command == "jmp":
            codeLine += int(value)
        if codeLine > len(data)-1:
            break
    if (repeatedLines == False) and (codeLine == len(data)):
        break

print(accumulator) */