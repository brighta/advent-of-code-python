import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getGrid(file):
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    return grid

def findXmas(grid):
    count = 0
    validOptions = ["MS", "SM"]
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if (grid[y][x] == "A"):
                if "{}{}".format(grid[y-1][x-1], grid[y+1][x+1]) in validOptions and "{}{}".format(grid[y-1][x+1], grid[y+1][x-1]) in validOptions:
                    count += 1
    return count

file = loadInput(fileName)
grid = getGrid(file)
count = findXmas(grid)
print(count)
