using System;
using System.IO;
using System.Text.RegularExpressions;
namespace c__d04
{
    class Program
    {
        static void Main(string[] args)
        {
         // Read data file
            string filename = "../d04-input.txt";
            string data = File.ReadAllText(filename);
            // Some passport info runs over two or more lines. Group each passport data 
            // onto single line seperated by a space
            string[] passports = data.Split(new string[] { "\n\n" }, StringSplitOptions.None);
         // Part 1 Solution
            int valid = 0;
            foreach (string passport in passports)
            {
                if (passport.Contains("byr") & passport.Contains("iyr") & passport.Contains("eyr") & passport.Contains("hgt") & passport.Contains("hcl") & passport.Contains("ecl") & passport.Contains("pid")) valid++;
            }
            Console.WriteLine("Part 1:");
            Console.WriteLine("In your batch file, how many passports are valid? {0}", valid);

        // Part 2 Solution
            valid = 0;
            foreach (string passport in passports)
            {
                string passportInfo = passport.Replace("\n", " ");
                string[] passportInfoParsed = passportInfo.Split(" ");
                string indx_iyr = "", indx_byr = "", indx_eyr = "", indx_hgt = "", indx_hcl = "", indx_ecl = "", indx_pid = "";
                foreach (string indx in passportInfoParsed)
                {
                    if (indx.Contains("iyr:")) indx_iyr = indx;
                    if (indx.Contains("byr:")) indx_byr = indx;
                    if (indx.Contains("eyr:")) indx_eyr = indx;
                    if (indx.Contains("hgt:")) indx_hgt = indx;
                    if (indx.Contains("hcl:")) indx_hcl = indx;
                    if (indx.Contains("ecl:")) indx_ecl = indx;
                    if (indx.Contains("pid:")) indx_pid = indx;
                }
                // if any of the indx_... are empty then invalid so skip to next passport
                if (indx_iyr.Equals("") | indx_byr.Equals("") | indx_eyr.Equals("") | indx_hgt.Equals("") | indx_hcl.Equals("") | indx_ecl.Equals("") | indx_pid.Equals("") ) continue;

                int byr = int.Parse(indx_byr.Split(":")[1]);
                int iyr = int.Parse(indx_iyr.Split(":")[1]);
                int eyr = int.Parse(indx_eyr.Split(":")[1]);
                string hgt = indx_hgt.Split(":")[1];
                string hcl = indx_hcl.Split(":")[1];
                string ecl = indx_ecl.Split(":")[1];
                string pid = indx_pid.Split(":")[1];

                // setup boolean variable for validity tests
                // validity test for birth year
                bool byr_valid = (byr >= 1920) & (byr <= 2002);
                // validity test for issue year
                bool iyr_valid = (iyr >= 2010) & (iyr <= 2020);
                // validity test for expiry year
                bool eyr_valid = (eyr >= 2020) & (eyr <= 2030);

                // setup Regex pattersn for hcl and pid
                string pattern = @"^#[0-9A-Fa-f]{6}$";
                Regex hclRegex = new Regex(pattern);
                bool hcl_valid = hclRegex.IsMatch(hcl);

                //validity test for eye colour
                bool ecl_valid = ecl.Equals("amb") | ecl.Equals("blu") | ecl.Equals("brn") | ecl.Equals("gry") | ecl.Equals("grn") | ecl.Equals("hzl") | ecl.Equals("oth");

                //validity test for passport ID
                pattern = @"\d{9}";
                Regex pidRegex = new Regex(pattern);
                bool pid_valid = pidRegex.IsMatch(pid);
                
                // validity tests for height
                // if hgt units missing invalid entry so skip to next, hgt.Substring(hgt.Length-2,2) returns units
                if (!(hgt.Substring(hgt.Length-2,2).Equals("cm") | hgt.Substring(hgt.Length-2,2).Equals("in"))) continue;
                // seperate the value and the units
                // value part = hgt.Substring(0, hgt.Length-2)
                // unit part = hgt.Substring( hgt.Length - 2, 2)
                int hgt_value = int.Parse(hgt.Substring(0,hgt.Length-2));
                string hgt_units = hgt.Substring(hgt.Length-2,2);
                bool hgt_valid = (hgt_value >= 150 & hgt_value <= 192 & hgt_units.Equals("cm")) | (hgt_value >= 59 & hgt_value <= 76 & hgt_units.Equals("in"));

                //if all the tests are valid then the passport is counted as a valid passport
                if (byr_valid & iyr_valid & eyr_valid & hcl_valid & ecl_valid & pid_valid & hgt_valid) valid++;



            }
            Console.WriteLine("Part 2:");
            Console.WriteLine("In your batch file, how many passports are valid? {0}", valid);

        }
    }
}
