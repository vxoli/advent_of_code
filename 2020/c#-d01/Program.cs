using System;
using System.IO;

namespace c__d01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Part 1");
            var filename = "../d01p1-input.txt";
            var data = File.ReadAllLines(filename);
            for (int i = 0; i < data.Length; i++)
            {
                for (int j = 0; j < data.Length; j++)
                {
                    if (int.Parse(data[i]) + int.Parse(data[j]) == 2020) Console.WriteLine(data[i],data[j], (int.Parse(data[i])*int.Parse(data[j])));
                }
            }
            Console.WriteLine("Part 2");
            for (int i = 0; i < data.Length; i++)
            {   for (int j = 0; j < data.Length; j++)
                {   for (int k = 0; k < data.Length; k++)
                    {
                        if (int.Parse(data[i]) + int.Parse(data[j]) + int.Parse(data[k]) == 2020) Console.WriteLine(data[i],data[j],data[k], (int.Parse(data[i]) * int.Parse(data[j]) * int.Parse(data[k])));
                    }
                }
            }

        }
    }
}
