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

def getDistances(lists):
    distances = []
    for i in range(len(lists[0])):
        distances.append(abs(lists[0][i]-lists[1][i]))
    return distances

file = loadInput(fileName)
lists = getLists(file)
distances = getDistances(lists)
print(sum(distances))