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

file = loadInput(fileName)
grid = generateGrid(file)
start = Coordinate(0, 0)#findLetter("S", grid)
grid[start.y][start.x] = "a"
coordinates = [str(start)]
end = findLetter("E", grid)
count = 1
while True:
    nextCoordinates = set()
    for coordinate in coordinates:
        nextCoordinates.update(Coordinate(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])).get_adjacents(grid))
    if str(end) in nextCoordinates:
        print(count)
        exit(0)
    coordinates = nextCoordinates
    count += 1
