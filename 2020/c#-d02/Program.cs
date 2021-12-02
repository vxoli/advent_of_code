using System;
using System.IO;
namespace c__d02
{
    class Program
    {
        static void Main(string[] args)
        {
		string filename = "../d02-input.txt";
		string[] data = File.ReadAllLines(filename);

		var counterPart1 = 0;
		var counterPart2 = 0;

		foreach (string line in data)
		{	// 2-9 c: cccccccc
			var fstSplit = line.Split(':'); // [0] 2-9 c, [1] _ccccccc
			var sndSplit = fstSplit[0].Split(' '); // [0] 2-9, [1] c
			var trdSplit = sndSplit[0].Split('-'); // [0] 2, [1] 9
			Int16 minimum = short.Parse(trdSplit[0]); // 2
			Int16 maximum = short.Parse(trdSplit[1]); // 9
			String character = sndSplit[1]; // c
			String password = fstSplit[1][1..]; // cccccccc
			var numberCharacters = password.Split(character).Length -1;
			if (numberCharacters >= minimum && numberCharacters <= maximum) counterPart1++;
			if ( (String.Equals(password[minimum-1], character[0]) && !String.Equals(password[maximum-1], character[0])) | (!String.Equals(password[minimum-1], character[0]) && String.Equals(password[maximum-1], character[0])) )  counterPart2++;
			{
				
			}
		}
		Console.WriteLine("Solution Part 1:");
		Console.WriteLine("Number of valid passwords is: {0}", counterPart1);
		Console.WriteLine("Solution Part 2:");
		Console.WriteLine("Number of valid passwords is: {0}", counterPart2);

        }
    }
}
