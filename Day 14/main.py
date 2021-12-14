# https://adventofcode.com/2021/day/14
import os
import string
from collections import Counter


def applyStep(pairs, rules):
    newPairs = dict.fromkeys(pairs.keys(), 0)
    for key, count in pairs.items():
        if count == 0:
            continue
        found = False
        for rule, ch in rules:
            if key == rule:
                newPairs[rule[0] + ch] += count
                newPairs[ch + rule[1]] += count
                found = True
                break
        if not found:
            newPairs[key] += count
    return newPairs


def getLetterCount(manual, pairs):
    counter = Counter()
    for key, value in pairs.items():
        if value:
            counter.update({key[0]: value})
            counter.update({key[1]: value})
    counter.update(manual[0])
    counter.update(manual[-1])
    return counter


def solvePart1(manual, pairs, rules):
    answer = 0
    for _ in range(10):
        pairs = applyStep(pairs, rules)

    counter = getLetterCount(manual, pairs)
    answer = (max(counter.values()) - min(counter.values())) // 2
    print("└─Part 01: ", answer)


def solvePart2(manual, pairs, rules):
    answer = 0
    for _ in range(40):
        pairs = applyStep(pairs, rules)

    counter = getLetterCount(manual, pairs)
    answer = (max(counter.values()) - min(counter.values())) // 2
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]

        pairs = {}
        for a in string.ascii_uppercase:
            for b in string.ascii_uppercase:
                pairs[a + b] = 0
        manual = data[0]
        for i in range(1, len(manual)):
            pairs[manual[i - 1 : i + 1]] += 1
        rules = [line.split(" -> ") for line in data[2:]]

        print("For " + filePath)
        solvePart1(manual, pairs, rules)
        solvePart2(manual, pairs, rules)


if __name__ == "__main__":
    DAY_PATH = "Day 14"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
