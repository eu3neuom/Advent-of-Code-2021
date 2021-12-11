# https://adventofcode.com/2021/day/11
import os

DX = [-1, 0, 1, 0, -1, -1, 1, 1]
DY = [0, -1, 0, 1, -1, 1, -1, 1]


def computeHighlight(data, stepNumber):
    global DX, DY

    energyLevels = [[int(el) for el in line] for line in data]
    n = len(energyLevels)
    m = len(energyLevels[0])

    highlights = 0
    firstFlash = -1
    for _ in range(stepNumber):
        for i in range(n):
            for j in range(m):
                energyLevels[i][j] += 1

        toHighlight = []
        marked = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if energyLevels[i][j] > 9:
                    toHighlight.append((i, j))
                    marked[i][j] = True

        for x, y in toHighlight:
            for dir in range(len(DX)):
                nx = x + DX[dir]
                ny = y + DY[dir]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or marked[nx][ny]:
                    continue

                energyLevels[nx][ny] += 1
                if energyLevels[nx][ny] > 9:
                    toHighlight.append((nx, ny))
                    marked[nx][ny] = True

        highlights += len(toHighlight)
        if len(toHighlight) == n * m and firstFlash == -1:
            firstFlash = _ + 1

        for i in range(n):
            for j in range(m):
                if energyLevels[i][j] > 9:
                    energyLevels[i][j] = 0

    return highlights, firstFlash


def solvePart1(data):
    answer, _ = computeHighlight(data, 100)
    print("└─Part 01: ", answer)


def solvePart2(data):
    _, answer = computeHighlight(data, 300)
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]

        print("For " + filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 11"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
