using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

/*
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
*/

namespace c__d11
{
    class Program
    {
        static void Main(string[] args)
        {
            //string filename = "../d11-input.txt";
            //string[] data = File.ReadAllLines(filename);
            string[] data = {"L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"}; // Test Data
            bool noChange = false;
            var seats = new List<string>();
            var seatsTemp = new List<string>();
            foreach (var row in data) seats.Add(row);
            while (!noChange)
            { // loop through each row and then each seat in that row
              // get seat value (occupied/ empty/ floor) and check 6 adjacent seats
              // apply seat change rules
              // repeat until list of seats doesnt change
              noChange = true;
                for (int row = 0; row <= seats.Count-1; row++)
                {
                    for (int seat = 0; seat <= seats[row].Length-1; seat++)
                    {
                        // seatValue could be empty (L) occupied (#) or floor (.)
                        const string Empty = "L";
                        const string Occupied = "#";
                        const string Floor = ".";
                        const string OOB = "X"; // oob => out-of-bounds;
                        var seatValue = seats[row][seat];
                        int[] seatPosn = {row,seat};
                        int seatsAdjacent = 0;
                        // calculate the co-ordinates of adjacent seats
                        // front = {row--, seat};
                        // left = {row, seat--};
                        // right = {row, seat++};
                        // back = {row++, seat};
                        // frontLeft = {row--, seat--};
                        // frontRight = {row--, seat++};
                        // backLeft = {row++, seat--};
                        // backRight = {row++, seat++};
                        // If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                        // Generate string of char to represent state of adjactent seatsAdjacent
                        // 1st char is front left, 2ns front, 3rd front right, 4th left, 6 myseat, 7th right, 8th back left, 9th back, 10th back right
                        string seatStatus = "";
                        seatStatus = string.Concat(seatStatus, ((row-- >= 0 & seat-- >=0) ? seats[row--][seat--] : OOB)); //front-left
                        seatStatus = string.Concat(seatStatus, ((row-- >= 0) ? seats[row--][seat] : OOB)); //front
                        seatStatus = string.Concat(seatStatus, ((row-- >= 0 & seat++ <= seats[0].Length-1) ? seats[row--][seat++] : OOB)); //front-right
                        seatStatus = string.Concat(seatStatus, ((seat-- >=0) ? seats[row][seat--] : OOB)); //left
                        seatStatus = string.Concat(seatStatus, seats[row][seat]); //the seat
                        seatStatus = string.Concat(seatStatus, ((seat++ <= seats[0].Length-1) ? seats[row][seat++] : OOB)); //right
                        seatStatus = string.Concat(seatStatus, ((row++ <= seats[0].Length-1 & seat-- >=0) ? seats[row++][seat--] : OOB)); //back-left
                        seatStatus = string.Concat(seatStatus, ((row++ <= seats[0].Length-1) ? seats[row++][seat] : OOB)); // back
                        seatStatus = string.Concat(seatStatus, ((row++ <= seats[0].Length-1 & seat <= seats[0].Length-1) ? seats[row++][seat++] : OOB)); //back-right
                        

  
                    }

                }


            }


        }
    }
}
