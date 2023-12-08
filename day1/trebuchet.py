'''
Author: Anthony Epps
Date: 12/7/23
AoC 2023: Day 1 Problem 1: Trebuchet
AoC 2023: Day 1 Problem 2: Trebuchet Part 2
'''

# Read in lines from text
def readPuzzle(list):
    with open("day1/puzzle.txt","r") as file:
        for line in file:
            line_filter = filter(str.isdigit, line)
            num = "".join(line_filter)
            list.append(num)
                # if char.isdigit():
                #     num += char
                #     list.append(num)


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

def writeListOutput(list):
    with open("day1/output.txt","w") as newfile:
        for lines in list:
            newfile.write(lines + "\n")

def main():
    print("Part One")
    list = []
    readPuzzle(list)
    total = parsePuzzleList(list)
    print(f"Total Value: {total}")
    writeListOutput(list)



if __name__ == "__main__":
    main()