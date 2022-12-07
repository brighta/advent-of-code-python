import sys
from classes import Directory
from classes import File

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()


def generatePathItems(file):
    pathItems = []
    currentPath = "/"
    i = 0
    while i < len(file):
        lineParts = file[i].rstrip().split(" ")
        if lineParts[1] == "cd":
            if lineParts[2] == "/":
                currentPath = "/"
            elif lineParts[2] == "..":
                currentPath = "/".join(currentPath.split("/")[0:-1])
            else:
                if currentPath == "/":
                    currentPath = "/" + lineParts[2]
                else:
                    currentPath += "/" + lineParts[2]
            i += 1
        else:
            i += 1
            while i < len(file) and file[i].split(" ")[0] != "$":
                lineParts = file[i].rstrip().split(" ")
                if lineParts[0] == "dir":
                    pathItems.append(Directory(currentPath, lineParts[1]))
                else:
                    pathItems.append(File(currentPath, lineParts[1], int(lineParts[0])))
                i += 1
    return pathItems


def getSizeOfDirectory(path, pathItems):
    count = 0
    for pathItem in pathItems:
        if pathItem.path == path:
            if pathItem.type == "f":
                count += pathItem.size
            else:
                count += getSizeOfDirectory(pathItem.get_directory_path(), pathItems)
    return count

file = loadInput(fileName)
pathItems = generatePathItems(file)
count = 0
for pathItem in pathItems:
    if pathItem.type == "d":
        size = getSizeOfDirectory(pathItem.get_directory_path(), pathItems)
        if size <= 100000:
            count += size
print(count)

