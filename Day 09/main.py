# https://adventofcode.com/2021/day/9
import os


DX = [-1, 0, 1, 0]
DY = [0, -1, 0, 1]


def markBasin(x, y, data, viz, id):
    global DX, DY

    area = 1
    viz[x][y] = id
    for dir in range(4):
        nx = x + DX[dir]
        ny = y + DY[dir]
        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
            continue
        if data[nx][ny] != "9" and viz[nx][ny] == -1:
            area += markBasin(nx, ny, data, viz, id)
    return area


def isSink(x, y, data):
    global DX, DY

    for dir in range(4):
        nx = x + DX[dir]
        ny = y + DY[dir]
        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
            continue
        if data[x][y] >= data[nx][ny]:
            return False
    return True


def getBasins(data):
    basinAreas = []
    sinkPoints = []
    n = len(data)
    m = len(data[0])
    viz = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == "9":
                continue
            if viz[i][j] == -1:
                basinAreas.append(markBasin(i, j, data, viz, len(basinAreas)))
                sinkPoints.append((-1, -1))
            if isSink(i, j, data):
                sinkPoints[viz[i][j]] = (i, j)
    return basinAreas, sinkPoints


def solvePart1(data):
    answer = 0
    _, sinkPoints = getBasins(data)
    for x, y in sinkPoints:
        answer += int(data[x][y]) + 1
    print("└─Part 01: ", answer)


def solvePart2(data):
    answer = 0
    basinAreas, _ = getBasins(data)
    basinAreas = sorted(basinAreas)
    answer = basinAreas[-1] * basinAreas[-2] * basinAreas[-3]
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]

        print("For " + filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 09"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
