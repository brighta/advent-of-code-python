import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getLists(file):
    list1 = []
    list2 = []
    for line in file:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
    list1.sort()
    list2.sort()
    return [list1, list2]

def getSimilarities(lists):
    similarities = []
    for number in lists[0]:
        similarities.append(number * lists[1].count(number))
    return similarities

file = loadInput(fileName)
lists = getLists(file)
similarities = getSimilarities(lists)
print(sum(similarities))