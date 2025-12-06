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
        newLines.append(line.split())
    for i in range(len(newLines[0])):
        question = []
        for j in range(len(newLines)):
            question.append(newLines[j][i] if j == len(newLines) - 1 else int(newLines[j][i]))
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