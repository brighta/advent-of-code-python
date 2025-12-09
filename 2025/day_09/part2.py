import sys

if len(sys.argv) < 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getCoordinates(lines):
    coordinates = []
    for line in lines:
        coordinates.append(tuple(list(map(int, line.rstrip().split(",")))))
    return coordinates

def getRectanglesSizes(coordinates):
    rectangleSizes = {}
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            coordinate1 = coordinates[i]
            coordinate2 = coordinates[j]
            rectangleSizes[(coordinate1, coordinate2)] = getRectangleSizes(coordinate1, coordinate2)
    return dict(sorted(rectangleSizes.items(), key=lambda item: item[1], reverse=True))

def getRectangleSizes(coordinate1, coordinate2):
    return (abs(coordinate1[0] - coordinate2[0]) + 1) *(abs(coordinate1[1] - coordinate2[1]) + 1)

def findLargestValidRectangle(rectangleSizes, coordinates):
    # count = 0
    for rectangleSize in rectangleSizes.keys():
        # count += 1
        # print("{:3} - {}".format(count, rectangleSize))
        corner1 = rectangleSize[0]
        corner2 = rectangleSize[1]
        linePoints = [(corner1[0], corner1[1]), (corner1[0], corner2[1]), (corner2[0], corner2[1]), (corner2[0], corner1[1])]
        if validRectangle(linePoints, coordinates):
           return rectangleSizes[rectangleSize]
    return 0

def validRectangle(linePoints, coordinates):
    for i in range(len(coordinates)):
        coordinate1 = coordinates[i]
        coordinate2 = coordinates[i + 1 if i < len(coordinates) - 1 else 0]
        if coordinate1 in linePoints or coordinate2 in linePoints:
            continue
        for points in [(linePoints[0], linePoints[1]), (linePoints[1], linePoints[2]), (linePoints[2], linePoints[3]), (linePoints[3], linePoints[0])]:
            # print("{} - {}".format(points, [coordinate1, coordinate2]))
            # print("{}-{}, {}-{}, {}-{}, {}-{} --> {}".format(points[0][0], points[0][1], points[1][0], points[1][1], coordinate1[0], coordinate1[1], coordinate2[0], coordinate2[1], linesIntercept(points[0][0], points[0][1], points[1][0], points[1][1], coordinate1[0], coordinate1[1], coordinate2[0], coordinate2[1])))
            if linesIntercept(points[0][0], points[0][1], points[1][0], points[1][1], coordinate1[0], coordinate1[1], coordinate2[0], coordinate2[1]):
                return False
    return True

def linesIntercept(x1, y1, x2, y2, x3, y3, x4, y4):
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    d = dx1 * dy2 - dy1 * dx2  # Determinant
    if d == 0:  # Parallel or Collinear
        return False  # For simplicity, treat collinear as non-intersecting segments
    # Calculate parameters s and t
    s = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / d
    t = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / d
    # Check if intersection point lies within both segments
    return 0 <= s <= 1 and 0 <= t <= 1

lines = loadInput(fileName)
coordinates = getCoordinates(lines)
rectangleSizes = getRectanglesSizes(coordinates)
# largestValidRectangle = findLargestValidRectangle({((9,5),(2,3)): 10}, coordinates)
largestValidRectangle = findLargestValidRectangle(rectangleSizes, coordinates)
print(largestValidRectangle)