using System;
using System.IO;
using System.Collections.Generic;
namespace c__d09
{
    class Program
    {
        static void Main(string[] args)
        {   //PART 1
            //read data file
            string[] data = File.ReadAllLines(@"../d09-input.txt");
            //test data
            //data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576];
            Int64[] numbers = Array.ConvertAll(data, s => Int64.Parse(s));
            int preamble = 25; // 25 for main proble, 5 for testing
            var xmasList = new List<Int64>();
            bool solution = false;
            for (int i = preamble; i == numbers.Length; i++)
            {//put next 25 numbers in a list
            xmasList.Clear();
            for (int j = 0; j < 25; j++) xmasList[j] = numbers[preamble+i+j-1];
            // use foreach loop to cycle through the lists of numbers
                solution = false;
                foreach (var num1 in xmasList) 
                {
                    foreach (var num2 in xmasList)
                    {
                        if ( (num1 + num2 == numbers[i]) && (num1 != num2) )
                        {
                            solution = true;
                            break;
                        }//end if
                    }//end k loop
                    if (solution == true) break;
                }//end j loop
                if (solution == false)
                {
                Console.WriteLine(i);
                break;
                }
            }//end i loop

        }
    }
}
/* # read data file
f = open('d09-input.txt', 'r')
data = f.readlines()
# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing
for i in range(0,len(data)):
    data[i] = int(data[i].strip("\n"))
# print(data[preamble:])

for idx, i in enumerate(data[preamble:]):
    solution = False
    # print("idx",idx,"i",i)
    for j in data[idx:idx+preamble]:
        for k in data[idx:idx+preamble]:
            if j + k == i and (j != k):
                # print("i",i,"j",j,"k",k)
                solution = True
                break
        if solution == True:
            break
    if solution == False:
        print(i)
        break
 */