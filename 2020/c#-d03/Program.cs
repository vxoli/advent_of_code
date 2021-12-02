using System;
using System.IO;
namespace c__d03
{
    class Program
    {
        static void Main(string[] args)
        {
//       Some of the code commented out as formed part of first solution
//      and then written into CountTrees function for part two solution.

            string[] map = File.ReadAllLines("../d03-input.txt");
            int trees = 0;
 //           int col = 0;
            int rowsTotal = map.GetLength(0);
            var length = map[0].Length;
//            for (int row = 0; row < rowsTotal; row++)
 //           {
 //               if (String.Equals(map[row][col], "#"[0])) trees++;
 //               col = (col+3) % (length);
 //           }
            Console.WriteLine("Part 1:");
            trees = CountTrees(3,1);
            Console.WriteLine("How many trees would you encounter? {0}", trees);
            Console.WriteLine("Part 2:");
            trees = CountTrees(1,1) * CountTrees(3,1) * CountTrees(5,1) * CountTrees(7,1) * CountTrees(1,2,2);
            Console.WriteLine("Product equals: {0}", trees);

        int CountTrees(int dx, int dy, int step = 1)
        {
            int treeCounter = 0;
            int x = 0;

            for (int y = step; y < map.Length; y += dy)
            {
                x += dx;
                if (x >= map[y].Length) x -= map[y].Length;
                if (map[y][x] == '#') treeCounter++;
            }
        return treeCounter;
        }

        }
    }
}
