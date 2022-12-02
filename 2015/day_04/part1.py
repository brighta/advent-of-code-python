import sys
from hashlib import md5

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def createMd5Hash(string):
    return md5(string.encode('utf-8')).hexdigest()

key = loadInput(fileName)[0].rstrip()
number = -1
hash = "11111"
while hash[0:5] != "00000":
    number += 1
    hash = createMd5Hash("{}{}".format(key, number))
print(number)
