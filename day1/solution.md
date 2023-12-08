# Solution (and random thoughts)

***Prompt***: The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number

For example:

1abc2

pqr3stu8vwx

a1b2c3d4e5f

treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

***Solution***: W.I.P

## Thoughts and Write Up

Since it's day one, I am going to use my comfort language: Python! (though Go might be better for this)

So, its a huge 1000 line text file, so lets just read in each line, iterate over it and check each digit to see if its a digit, if so add to new array, then add together.

I went with this thought and tried to do a bunch of nested loops to iterate over each line of text, within each line iterate over each character and see if its a digit, if it is then add. This was wonky and didnt work, so did some googling for better ways to parse digits from string, and landed on [this](https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python/73444103#73444103). I scrolled down to [Ehsan Akbaritabar](https://stackoverflow.com/users/12740851/ehsan-akbaritabar)'s response and their use of `filter` was PERFECT! Simple, efficient and "pythonic".

I then neeeded a way to make verify this was working as intended, so I did a simple write out to output.txt and was able to see I had succesfull parsed my numbers! Now I just had to reiterate over the list and add each line to a running total (after casting to int) based on the following conditions:
    - if len(line) > 2: Take line[0] and line[size-1] to get first and last digits
    - if len(line) == 1: Since we have 1 digit, it was just add another char of same digit. i.e. 1 => 11
    - else: Add to running total

Output the total and BOOM! WE got our answer :D!

If I was to rewrite this in another language, I would try it with Go. 

If I had to use Python again, I would try and use list comprehensions and maybe use `re` to filter the strings better

## Potential Problems: 
 - **Speed using Python versus other languages:** Yeah, that wasn't a problem at all LOL. Python made short work of the 1000 lines of text


