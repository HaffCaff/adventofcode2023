# Solution (and random thoughts)

***Prompt***: The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

***Solution***: W.I.P

## Thoughts

Since it's day one, I am going to use my comfort language: Python! (though Go might be better for this)

So, its a huge 1000 line text file, so lets just read in each line, iterate over it and check each digit to see if its a digit, if so add to new array, then add together

- Potential Problems: HECKA slow...especially using Python.
