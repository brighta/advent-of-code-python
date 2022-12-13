import sys
from ast import literal_eval

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateList(string):
    return literal_eval(string)

def removeFirstItem(list):
    if type(list[0]) == list and len(list[0]) != 1:
        newList = list[i][1:]
        newList.extend(list[1:])
        return newList
    return list[1:]

def isListInOrder(firstList, secondList):
    if len(firstList) == 0:
        if len(secondList) == 0:
            return None
        else:
            return True
    if len(secondList) == 0:
        return False
    if type(firstList[0]) == type(secondList[0]) == int:
        if firstList[0] < secondList[0]:
            return True
        elif firstList[0] > secondList[0]:
            return False
        else:
            if len(firstList) == len(secondList) == 1:
                return None
            return isListInOrder(removeFirstItem(firstList), removeFirstItem(secondList))
    if type(firstList[0]) == type(secondList[0]) == list:
        if len(firstList[0]) == 0:
            if len(secondList[0]) == 0:
                return isListInOrder(removeFirstItem(firstList), removeFirstItem(secondList))
            else:
                return True
        if len(secondList[0]) == 0:
            return False
        listIsInOrder = isListInOrder(firstList[0], secondList[0])
        if listIsInOrder == True or listIsInOrder == False:
            return listIsInOrder
        return isListInOrder(removeFirstItem(firstList), removeFirstItem(secondList))
    if type(firstList[0]) == int:
        newFirstList = [[firstList[0]]]
        newFirstList += firstList[1:]
        return isListInOrder(newFirstList, secondList)
    else:
        newSecondList = [[secondList[0]]]
        newSecondList += secondList[1:]
        return isListInOrder(firstList, newSecondList)

file = loadInput(fileName)
count = 0
index = 1
i = 0
while i < len(file):
    firstList = literal_eval(file[i].rstrip())
    secondList = literal_eval(file[i+1].rstrip())
    if isListInOrder(firstList, secondList):
        count += index
    index += 1
    i += 3
print(count)
