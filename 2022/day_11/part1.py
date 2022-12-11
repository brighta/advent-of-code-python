import sys
from classes import Monkey

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateMonkeys(file):
    monkeys = []
    i = 0
    while i < len(file):
        monkeys.append(Monkey(
            [int(item) for item in file[i+1].rstrip().split(": ")[1].split(", ")],
            file[i+2].rstrip().split(" ")[6],
            file[i+2].rstrip().split(" ")[7],
            file[i+3].rstrip().split(" ")[5],
            file[i+4].rstrip().split(" ")[9],
            file[i+5].rstrip().split(" ")[9]
        ))
        i += 7
    return monkeys

file = loadInput(fileName)
monkeys = generateMonkeys(file)
for monkey in monkeys:
    print(monkey)
for i in range(20):
    for monkey in monkeys:
        monkeys = monkey.perform_operations(monkeys, True)
monkeyBusinesses = [monkey.get_count() for monkey in monkeys]
monkeyBusinesses.sort(reverse=True)
print(str(monkeyBusinesses[0] * monkeyBusinesses[1]))
