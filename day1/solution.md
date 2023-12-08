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

Output the total and BOOM! WE got our answer :D... for part 1

Part required us to actually parse the whole string for potential words as well, which would then represent different starting or ending numbers. Here I decided to refactor my code into functions to make a bit easier to read and organize. So the rewrite started off really strong, I rewrote everything, decided to use a dictionary key:value to control swapping words to digits (i.e. one => 1). I rewrote how to total, how to print so I can have a side by side of problem one and problem 2 in my main output. I ran the code, checked the outpart2.txt file and smiled as everything was right. I submitted my new answer and it was wrong. What do you mean it is wrong? I then parsed the puzzle text and compared the output....and it was right!? What am I missing? After about 2 hours I gave up and looked at the hints subreddit. The first thing I see is the eighthree bug. I looked at it and had NO idea what it was talking about and then it clicked. The t was used for both eight and three, so depending on your solution you would end up with 8hee or eigh3. I laughed a bit because of constant theme of first and last and how here it jammed you by replaceing a number right between the first...and...last...letters....WAIT A MINUTE. Instead of having the eight return 8 or three return 3, why not have it return t3e, the first letter, number, and last letter. BOOM I felt like a genius and gave it a shot. It did not work. Again I was FURIOUS and after about an hour I succumbed to the darkness and went to the spoilers section. What do I see? Alot of other people had the same idea, except they did it for ALL the numbers...DUH. I felt silly and somewhat proud as I assume most people on the subreddit and others participating are SIGNIFICANTLY further along in their careers, so I feel like I am at least on the right track. However...this was problem one, and I am still in the midst of finals...so this is going to be an adventure finishing, but I am at least going to try!

If I was to rewrite this in another language, I would try it with Go. 

If I had to use Python again, I would try and use list comprehensions and maybe use `re` to filter the strings better

## Potential Problems: 
 - **Speed using Python versus other languages:** Yeah, that wasn't a problem at all LOL. Python made short work of the 1000 lines of text


