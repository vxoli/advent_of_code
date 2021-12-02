using System;
using System.IO;
using System.Linq;

namespace c__d01_v2
{
    class Program
    {
        static void Main(string[] args)
        {
            var filename = "../d01p1-input.txt";
            var data = File.ReadAllLines(filename);
            var part1 = (
            from p in data
            from q in data
                where (int.Parse(p) + int.Parse(q)) == 2020
                select (p, q));
            var part2 = (
            from p in data
            from q in data
            from r in data
                where (int.Parse(p) + int.Parse(q) + int.Parse(r)) == 2020
                select (p, q,r));
            Int64 answer1 = 1, answer2 = 1;
            foreach (var num in part1) answer1 = answer1 * Int64.Parse(num.p);
            foreach (var num in part2) answer2 = answer2 * Int64.Parse(num.p);

            Console.WriteLine($"Part 1: {answer1}");
            Console.WriteLine($"Part 2: {answer2}");

        }
    }
}