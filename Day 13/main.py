# https://adventofcode.com/2021/day/13
import os


def makeFold(points, fold):
    axis, dist = fold
    if axis == "y":
        newPoints = [(x, y) if y < dist else (x, dist - (y - dist)) for x, y in points]
    else:
        newPoints = [(x, y) if x < dist else (dist - (x - dist), y) for x, y in points]
    return list(dict.fromkeys(newPoints))


def solvePart1(points, folds):
    answer = 0
    points = makeFold(points, folds[0])
    answer = len(points)
    print("└─Part 01: ", answer)


def solvePart2(points, folds):
    for fold in folds:
        points = makeFold(points, fold)

    DISPLAYX = max([x for _, x in points]) + 1
    DISPLAYY = max([x for x, _ in points]) + 1
    display = [["_" for _ in range(DISPLAYY)] for _ in range(DISPLAYX)]
    for (x, y) in points:
        display[y][x] = "#"

    print("└─Part 02: ")
    for line in display:
        print("".join(line))


def solveProblem(filePath):
    with open(filePath, "r") as file:
        points, folds = [], []
        for line in file.readlines():
            if "," in line:
                x, y = line.split(",")
                points.append((int(x), int(y)))
            if "=" in line:
                axis, dist = line.split("=")
                folds.append((axis[-1], int(dist)))

        print("For " + filePath)
        solvePart1(points, folds)
        solvePart2(points, folds)


if __name__ == "__main__":
    DAY_PATH = "Day 13"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
