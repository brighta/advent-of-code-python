import sys
from classes import Coordinate

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateGrid(file):
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    return grid

def findLetter(letter, grid):
    for i in range(len(grid)):
        if letter in grid[i]:
            return Coordinate(grid[i].index(letter), i)

def findAllLetter(letter, grid):
    letters = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == letter:
                letters.append(Coordinate(x, y))
    return letters

file = loadInput(fileName)
grid = generateGrid(file)
start = findLetter("S", grid)
grid[start.y][start.x] = "a"
starts = findAllLetter("a", grid)
end = findLetter("E", grid)
print("Number Starts : " + str(len(starts)))
minCount = 330
for i in range(len(starts)):
    start = starts[i]
    count = 1
    complete = False
    coordinates = [str(start)]
    while not complete:
        nextCoordinates = set()
        for coordinate in coordinates:
            nextCoordinates.update(Coordinate(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])).get_adjacents(grid))
        if str(end) in nextCoordinates:
            complete = True
            if count < minCount:
                minCount = count
        elif count >= minCount:
            complete = True
        else:
            coordinates = nextCoordinates
            count += 1
    print("#" + str(i) + " - " + str(count))
print(minCount)
