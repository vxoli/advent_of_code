using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace c__d07
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines("../d07-input.txt");
            //split lines into bag colour and what that bag can contain
            //select the bags that can contain shiny gold bags
            string bagColour, bagContents;
            var myBags = new List<string>();
            var moreBags = new List<string>();
            int index = 0;
            foreach (string line in data)
            {
                bagColour = line.Split(" contain ")[0];
                bagContents = line.Split(" contain ")[1];
                if (bagContents.Contains("shiny gold")) myBags.Add(bagColour.Substring(0,bagColour.Length-5));
            }
            //find the bags that can contain bags that contain shiny gold bags
            foreach (string bag in myBags)
            {Console.WriteLine(bag);
                foreach (string line in data)
                {
                    bagColour = line.Split(" contain ")[0];
                    bagContents = line.Split(" contain ")[1];
                    if (bagContents.Contains(bag)) moreBags.Add(bagColour.Substring(0,bagColour.Length-5));
                }
            }
            foreach (var line in myBags)
            {
                Console.WriteLine(line+"~");
                index++;
            }
            foreach (var line in moreBags)
            {
                Console.WriteLine(line+"+");
                index++;
            }
            // remove duplicates
            //List<T> noDupes = withDupes.Distinct().ToList();
            Console.WriteLine(index);
        }
    }
}
//f = open('d07-input.txt', 'r')
//data = f.readlines()
//# data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.", "dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "bright white bags contain 1 shiny gold bag." , "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags." , "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags." , "dark olive bags contain 3 faded blue bags, 4 dotted black bags.", "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags." , "faded blue bags contain no other bags.", "dotted black bags contain no other bags."]
//myBags = []
//data_clean = [data[i].split("contain") for i in range(len(data))]

//# find the bags that can contain "shiny gold bags"
//myBags = [data_clean[s][0][0:len(data_clean[s][0])-6] for s in range(len(data_clean)) if "shiny gold" in data_clean[s][1]]

//# find bags that can contain bags that can contain "shiny gold bags"
//for bag_col in myBags:
//	myBags += [data_clean[s][0][0:len(data_clean[s][0])-6] for s in range(len(data_clean)) if bag_col in data_clean[s][1]]

//# remove duplicate bag colours
//myBags = list(dict.fromkeys(myBags))	
//print(myBags)
//print(len(myBags))