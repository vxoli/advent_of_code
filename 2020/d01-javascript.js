// Reading the file and converting it to int
const fs = require('fs')
var ipt = fs.readFileSync("d01p1-input.txt", 'utf8').split("\n").filter(x => x.length != 0);
ipt = ipt.map(x => parseInt(x));
// Part 1
for (i of ipt) {
    for (j of ipt) {
        if (i + j == 2020) {
            console.log(i + " " + j + " " + (i+j))
        }
    }
}
// Part 2
for (i of ipt) {
    for (j of ipt) {
        for (k of ipt){
            if (i + j + k == 2020) {
            console.log(i + " " + j + " " + " ", k, " " + (i+j+k))
            }
        }
    }
}