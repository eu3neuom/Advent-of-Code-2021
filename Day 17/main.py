# https://adventofcode.com/2021/day/17
import os


def inTargetArea(targetArea, velX, velY):
    x, y = 0, 0
    areax, areaX = targetArea[0]
    areay, areaY = targetArea[1]
    maxY = 0
    while x <= areaX and y >= areay:
        if areax <= x <= areaX and areay <= y <= areaY:
            return maxY
        x, y = x + velX, y + velY
        velX, velY = max(0, velX - 1), velY - 1
        maxY = max(maxY, y)
    return -1


def generateVelocities(targetArea):
    MIN_VELX, MAX_VELX = -300, 300
    MIN_VELY, MAX_VELY = -300, 300
    for velocityX in range(MIN_VELX, MAX_VELX):
        for velocityY in range(MIN_VELY, MAX_VELY):
            maxY = inTargetArea(targetArea, velocityX, velocityY)
            if maxY != -1:
                yield maxY, velocityX, velocityY


def solveBothParts(targetArea):
    answertPart1 = 0
    unique = set()
    for maxY, velocityX, velocityY in generateVelocities(targetArea):
        answertPart1 = max(answertPart1, maxY)
        unique.add((velocityX, velocityY))
    answerPart2 = len(unique)
    print("└─Part 01: ", answertPart1)
    print("└─Part 02: ", answerPart2)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]
        data = data[0].replace(",", "").replace("..", " ").replace("=", " ").split(" ")
        targetArea = [(int(data[3]), int(data[4])), (int(data[6]), int(data[7]))]

        print("For " + filePath)
        solveBothParts(targetArea)


if __name__ == "__main__":
    DAY_PATH = "Day 17"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
