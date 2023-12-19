import sys
import re
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    rules = {}
    for fileLine in fileLines:
        if fileLine == '':
            return rules
        key = fileLine.split('{')[0]
        ruleComponents = fileLine.split('{')[1].split('}')[0].split(',')
        ruleParts = []
        for ruleComponent in ruleComponents[:-1]:
            regex = list(re.findall('(x|m|a|s)(<|>)([0-9]+):([a-zAR]*)', ruleComponent)[0])
            regex[2] = int(regex[2])
            ruleParts.append(regex)
        ruleParts.append(ruleComponents[-1])
        rules[key] = ruleParts

def getRangesForRule(rules, ruleLetter, part):
    answer = 0
    for rule in rules[ruleLetter][:-1]:
        range = part[rule[0]]
        newRange = None
        if rule[1] == '<':
            if range[0] < rule[2]:
                if range[1] < rule[2]:
                    newRange = (range[0], range[1])
                else:
                    newRange = (range[0], rule[2] - 1)
                    range = (rule[2], range[1])
        else:
            if range[1] > rule[2]:
                if range[0] > rule[2]:
                    newRange = (range[0], range[1])
                else:
                    newRange = (rule[2] + 1, range[1])
                    range = (range[0], rule[2])
        if newRange is not None:
            newPart = part.copy()
            newPart[rule[0]] = newRange
            if rule[3] == 'A':
                answer += math.prod([range[1] - range[0] + 1 for range in newPart.values()])
            elif rule[3] != 'R':
                answer += getRangesForRule(rules, rule[3], newPart)
        part[rule[0]] = range
    if rules[ruleLetter][-1] == 'A':
        answer += math.prod([range[1] - range[0] + 1 for range in part.values()])
    elif rules[ruleLetter][-1] != 'R':
        answer += getRangesForRule(rules, rules[ruleLetter][-1], part)
    return answer

def getAnswer(rules):
    part = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    return getRangesForRule(rules, 'in', part)


fileLines = loadInput(fileName)
rules = getPuzzleInput(fileLines)
answer = getAnswer(rules)
print(answer)
