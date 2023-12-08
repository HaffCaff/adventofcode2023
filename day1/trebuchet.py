'''
Author: Anthony Epps
Date: 12/7/23
AoC 2023: Day 1 Problem 1: Trebuchet
AoC 2023: Day 1 Problem 2: Trebuchet Part 2
'''

# Read in lines from text, filter and add to list
def readPuzzle(list):
    with open("day1/puzzle.txt","r") as file:
        for line in file:
            line_filter = filter(str.isdigit, line)
            num = "".join(line_filter)
            list.append(num)
                # if char.isdigit():
                #     num += char
                #     list.append(num)
# Iterate over string and swap all words with corresponding number
def wordToDigit(string):
    worddict = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
        'zero': 'z0o'
    }
    newstring = string
    for word, digit in worddict.items():
        newstring = newstring.replace(word,digit)
    return newstring


# Part Two Implementation of read puzzle, left original solution so others could see train of thought
def readPuzzleBetter(list):
    # words = ["one", "two","three","four","five","six","seven","eight","nine","zero"] after typing this out I realized a dict would probably be better
    with open("day1/puzzle.txt","r") as file:
        for line in file:
            convertedLine = wordToDigit(line)
            lineFilter = filter(str.isdigit, convertedLine)
            num = "".join(lineFilter)
            list.append(num)

            
# Formate the list and 
def parsePuzzleList(list):
    total = 0
    for lines in list:
        if len(lines) > 2:
            newline = ""
            newline += lines[0]
            newline += lines[len(lines)-1]
            total += int(newline)
        elif len(lines) == 1:
            newline = ""
            newline += lines[0]
            newline += lines[0]
            total += int(newline)
        else:    
            total += int(lines)
    return total

def parsePuzzleListBetter(list):
    newlist = []
    for lines in list:
        size = len(lines)
        if size > 2:
            newline = ""
            newline += lines[0]
            newline += lines[-1]
            newlist.append(newline)
        elif size == 1:
            newline = ""
            newline += lines[0]
            newline += lines[0]
            newlist.append(newline)
        else:
            newlist.append(lines)
    return newlist

def getTotal(list):
    total = 0
    for lines in list:
        total += int(lines)
    return total



def writeListOutput(list):
    with open("day1/output.txt","w") as newfile:
        for lines in list:
            newfile.write(lines + "\n")


def writeListOutputAgain(list):
    with open("day1/outputpart2.txt","w") as newfile:
        for lines in list:
            newfile.write(lines + "\n")


def main():
    list = []
    print("Part One")
    readPuzzle(list)
    total = parsePuzzleList(list)
    print(f"Total Value: {total}")
    writeListOutput(list)

    print()

    list1 = []
    print("Part Two")
    readPuzzleBetter(list1)
    parsed = parsePuzzleListBetter(list1)
    writeListOutputAgain(parsed)
    total1 = getTotal(parsed)
    print(f"Total Value of Part 2: {total1}")

    # print("Tests")
    # list = []
    # test = "onetwo3"
    # print ("Before: " + test)
    # #test = test.replace("one","1")
    # test1 = wordToDigit(test)
    # print ("After: " + test1)
    # #print (test1)



if __name__ == "__main__":
    main()