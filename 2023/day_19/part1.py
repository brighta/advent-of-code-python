import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    rules = {}
    parts = []
    inRules = True
    for fileLine in fileLines:
        if fileLine == '':
            inRules = False
        elif inRules:
            key = fileLine.split('{')[0]
            ruleComponents = fileLine.split('{')[1].split('}')[0].split(',')
            ruleParts = []
            for ruleComponent in ruleComponents[:-1]:
                regex = list(re.findall('(x|m|a|s)(<|>)([0-9]+):([a-zAR]*)', ruleComponent)[0])
                regex[2] = int(regex[2])
                ruleParts.append(regex)
            ruleParts.append(ruleComponents[-1])
            rules[key] = ruleParts
        else:
            part = {}
            for partComponent in fileLine[1:-1].split(','):
                partComponentBits = partComponent.split('=')
                part[partComponentBits[0]] = int(partComponentBits[1])
            parts.append(part)
    return rules, parts

def getAnswer(rules, parts):
    accepted = []
    for part in parts:
        currentRule = 'in'
        while currentRule != 'A' and currentRule != 'R':
            newRule = None
            for rule in rules[currentRule][:-1]:
                partValue = part[rule[0]]
                if rule[1] == '<':
                    if partValue < rule[2]:
                        newRule = rule[3]
                        break
                else:
                    if partValue > rule[2]:
                        newRule = rule[3]
                        break
            if newRule is None:
                newRule = rules[currentRule][-1]
            currentRule = newRule
        if currentRule == 'A':
            accepted.append(part)
        answer = 0
    for part in accepted:
        answer += part['x'] + part['m'] + part['a'] + part['s']
    return answer


fileLines = loadInput(fileName)
rules, parts = getPuzzleInput(fileLines)
answer = getAnswer(rules, parts)
print(answer)
