import sys
from math import prod

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getQuestions(lines):
    questions = []
    newLines = []
    for line in lines:
        newLines.append(list(line.rstrip()))
    maxLen = max(map(len, map(str.rstrip, lines)))
    for i in range(len(newLines)):
        newLines[i].extend([" "] * (maxLen - len(newLines[i])))
    numRowsOfNumbers = len(newLines) - 1
    question = []
    for i in range(len(newLines[0]) - 1, -1, -1):
        numberString = ""
        for j in range(numRowsOfNumbers):
            numberString += newLines[j][i]
        if numberString == " " * numRowsOfNumbers:
            question.append(newLines[-1][i + 1])
            questions.append(question)
            question = []
        else:
            question.append(int(numberString))
    question.append(newLines[-1][0])
    questions.append(question)
    return questions

def solveQuestions(questions):
    answers = []
    for question in questions:
        if question[-1] == "+":
            answers.append(sum(question[:-1]))
        elif question[-1] == "*":
            answers.append(prod(question[:-1]))
    return answers


lines = loadInput(fileName)
questions = getQuestions(lines)
answers = solveQuestions(questions)
print(sum(answers))