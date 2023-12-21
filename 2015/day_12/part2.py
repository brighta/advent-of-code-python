import sys
import json

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read()

def countInJson(object):
    answer = 0
    if type(object) == dict:
        if "red" in object.values():
            return 0
    for item in object if type(object) == dict else range(len(object)):
        if type(object[item]) == dict:
            answer += countInJson(object[item])
        elif type(object[item]) == list:
            for listItem in object[item]:
                if type(listItem) == int:
                    answer += listItem
                elif type(listItem) != str:
                    answer += countInJson(listItem)
        elif type(object[item]) == int:
            answer += object[item]
    return answer

def getAnswer(input):
    object = json.loads(input)
    return countInJson(object)

input = loadInput(fileName)
answer = getAnswer(input)
print(answer)
