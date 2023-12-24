import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    hails = []
    for fileLine in fileLines:
        hailParts = fileLine.split(' @ ')
        hails.append([list(map(int, hailParts[0].split(', ')[:-1])), list(map(int, hailParts[1].split(', ')[:-1]))])
    return hails

def getEdges(hails, minimum, maximum):
    for hail in hails:
        if hail[1][0] > 0:
            numTimes = math.floor((maximum - hail[0][0]) / hail[1][0])
        else:
            numTimes = math.floor((hail[0][0] - minimum) / hail[1][0] * -1)
        xCoords = [hail[0][0] + hail[1][0] * numTimes, hail[0][1] + hail[1][1] * numTimes]
        if minimum <= xCoords[1] <= maximum:
            hail.append(xCoords)
        else:
            if hail[1][1] > 0:
                numTimes = math.floor((maximum - hail[0][1]) / hail[1][1])
            else:
                numTimes = math.floor((hail[0][1] - minimum) / hail[1][1] * -1)
            yCoords = [hail[0][0] + hail[1][0] * numTimes, hail[0][1] + hail[1][1] * numTimes]
            hail.append(yCoords)
    return hails

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return None
def getIntersections(hails, minimum, maximum):
    answer = 0
    for i in range(len(hails)):
        for j in range(i + 1, len(hails)):
            hail1 = hails[i]
            hail2 = hails[j]
            l1 = line(hail1[0], hail1[2])
            l2 = line(hail2[0], hail2[2])
            p = intersection(l1, l2)
            hail1minX = min([hail1[0][0], hail1[2][0]])
            hail1maxX = max([hail1[0][0], hail1[2][0]])
            hail2minX = min([hail2[0][0], hail2[2][0]])
            hail2maxX = max([hail2[0][0], hail2[2][0]])
            if p is not None and minimum <= p[0] <= maximum and minimum <= p[1] <= maximum and hail1minX <= p[0] <= hail1maxX and hail2minX <= p[0] <= hail2maxX:
                answer += 1
    return answer



fileLines = loadInput(fileName)
hails = getPuzzleInput(fileLines)
minimum = 7 if 'sample' in fileName else 200000000000000
maximum = 27 if 'sample' in fileName else 400000000000000
hails = getEdges(hails, minimum, maximum)
answer = getIntersections(hails, minimum, maximum)
print(answer)