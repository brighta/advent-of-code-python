import sys
import itertools

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    people = []
    happinesses = {}
    for line in fileLines:
        person1 = line.split(' ')[0]
        person2 = line.split(' ')[-1][:-1]
        happiness = int(line.split(' ')[3]) * (-1 if line.split(' ')[2] == 'lose' else 1)
        if person1 in people:
            happinesses[person1][person2] = happiness
        else:
            people.append(person1)
            happinesses[person1] = {person2: happiness}
    return people, happinesses

def getAnswer(people, happinesses):
    maxAnswer = 0
    for path in list(itertools.permutations(people)):
        answer = 0
        current = path[0]
        for next in path[1:]:
            answer += happinesses[current][next]
            answer += happinesses[next][current]
            current = next
        answer += happinesses[path[-1]][path[0]]
        answer += happinesses[path[0]][path[-1]]
        maxAnswer = max(maxAnswer, answer)
    return maxAnswer


fileLines = loadInput(fileName)
people, happinesses = getPuzzleInput(fileLines)
answer = getAnswer(people, happinesses)
print(answer)
