import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    input = []
    for fileLine in fileLines:
        input.append(list(map(int, list(fileLine))))
    return input

class Node():
    def __init__(self, parent=None, position=None, facing='*', numberMovesForwards=0):
        self.parent = parent
        self.position = position
        self.facing = facing
        self.numberMovesForwards = numberMovesForwards
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, facing, end):
    startNode = Node(parent=None, position=start, facing=facing)
    endNode = Node(parent=None, position=end)
    openList = []
    closedList = []
    openList.append(startNode)
    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index
        openList.pop(currentIndex)
        closedList.append(currentNode)
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        if currentNode.facing == 'N' or currentNode.facing == 'S':
            newPositions = [(0, 1, 'E', 0), (-1 if currentNode.facing == 'N' else 1, 0, currentNode.facing, currentNode.numberMovesForwards + 1), (0, -1, 'W', 0)]
        else:
            newPositions = [(1, 0, 'S', 0), (0, -1 if currentNode.facing == 'W' else 1, currentNode.facing, currentNode.numberMovesForwards + 1), (-1, 0, 'N', 0)]
        for newPosition in newPositions:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
            if nodePosition[0] > len(maze) - 1 or nodePosition[0] < 0 or nodePosition[1] > len(maze[0]) - 1 or nodePosition[1] < 0:
                continue
            if newPosition[3] > 2:
                continue
            newNode = Node(parent=currentNode, position=(nodePosition[0], nodePosition[1]), facing=newPosition[2], numberMovesForwards=newPosition[3])
            children.append(newNode)
        for child in children:
            for closedChild in closedList:
                if child == closedChild:
                    continue
            child.g = currentNode.g + maze[child.position[0]][child.position[1]]
            child.h = (abs(child.position[0] - endNode.position[0]) + abs(child.position[1] - endNode.position[1])) * 4.5
            child.f = child.g + child.h
            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue
            openList.append(child)


fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
path = astar(grid, (0, 0), 'E', (len(grid) - 1, len(grid[0]) - 1))
answer = 0
for position in path[1:]:
    answer += grid[position[0]][position[1]]
print(answer)
