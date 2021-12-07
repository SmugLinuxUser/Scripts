import re
import sys
import fileinput


filehandler = open("/home/joseph/Desktop/puzzleinput.txt", "rt")
passCount = 0
Count = 0
for line in filehandler:
    passCount += 1
    lowerlimit = re.search(".+?(?=-)", line)
    upperlimit = re.search("(?<=-)\d*", line)
    Rqletter = re.search("[a-z]", line)
    password = re.search("(?<=:\s)[a-z]*", line)
    N = password.group().count(Rqletter.group())
    if N > int(lowerlimit.group()) and N < int(upperlimit.group()):
        Count += 1 
print(Count, "out of", passCount)
    

    


filehandler.close()

