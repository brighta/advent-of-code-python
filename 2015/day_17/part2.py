import sys
import itertools

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    return list(map(int, fileLines))

def getAnswer(containers, total):
    answers = {}
    options = []
    for r in range(1, len(containers)):
        options.extend([list(object) for object in list(itertools.combinations(containers, r))])
    for option in options:
        if sum(option) == total:
            if len(option) in answers:
                answers[len(option)] += 1
            else:
                answers[len(option)] = 1
    return answers[min(answers.keys())]


fileLines = loadInput(fileName)
containers = getPuzzleInput(fileLines)
answer = getAnswer(containers, 25 if 'sample' in fileName else 150)
print(answer)
