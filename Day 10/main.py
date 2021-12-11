# https://adventofcode.com/2021/day/10
import os
from enum import Enum, unique


@unique
class ChunkType(Enum):
    ILLEGAL = 0
    INCOMPLETE = 1


def solve(line):
    queue = []
    expectedPair = {")": "(", "]": "[", "}": "{", ">": "<"}
    value = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for ch in line:
        if ch in expectedPair.values():
            queue.append(ch)
        else:
            if expectedPair[ch] == queue[-1]:
                queue.pop()
            else:
                return ChunkType.ILLEGAL, value[ch]

    matchingCost = 0
    value = {"(": 1, "[": 2, "{": 3, "<": 4}
    for ch in reversed(queue):
        matchingCost = matchingCost * 5 + value[ch]

    return ChunkType.INCOMPLETE, matchingCost


def solvePart1(data):
    answer = 0
    for line in data:
        type, cost = solve(line)
        if type == ChunkType.ILLEGAL:
            answer += cost
    print("└─Part 01: ", answer)


def solvePart2(data):
    answer = []
    for line in data:
        type, cost = solve(line)
        if type == ChunkType.INCOMPLETE:
            answer.append(cost)
    answer = sorted(answer)[int(len(answer) / 2)]
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]

        print("For " + filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 10"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
