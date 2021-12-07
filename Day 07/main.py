# https://adventofcode.com/2021/day/7
import os


def getMinCost(data, formula):
    minCost = sum(data) ** 3
    for target in range(min(data), max(data)):
        cost = 0
        for num in data:
            dif = abs(target - num)
            cost += formula(dif)
        minCost = min(minCost, cost)
    return minCost


def solvePart1(data):
    answer = getMinCost(data, lambda x: int(x))
    print("└─Part 01: ", answer)


def solvePart2(data):
    answer = getMinCost(data, lambda x: int(x * (x + 1) / 2))
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [int(num) for num in file.readline().split(",")]

        print("For " + filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 07"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
