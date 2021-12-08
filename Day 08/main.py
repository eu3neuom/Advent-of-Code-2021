# https://adventofcode.com/2021/day/8
import os
from itertools import permutations


def solvePart1(data):
    answer = 0
    for line in data:
        signalsOut = line.split("|")[1].split()
        for signal in signalsOut:
            if len(signal) in [2, 4, 3, 7]:
                answer += 1

    print("└─Part 01: ", answer)


SIGNALS = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def convertSignal(signal, mapping):
    return "".join([mapping[ch] for ch in signal])


def getDigit(signal, expectedSignals):
    signal = "".join(sorted(signal))
    for i, expectedSignal in enumerate(expectedSignals):
        if signal == expectedSignal:
            return i


def validPermutation(signals, expectedSignals):
    for signal in signals:
        signal = "".join(sorted(signal))
        if signal not in expectedSignals:
            return False
    return True


def solvePart2(data):
    answer = 0
    for line in data:
        signalsIn = line.split("|")[0].split()
        signalsOut = line.split("|")[1].split()
        for perm in list(permutations("abcdefg")):
            mapping = {}
            for i, ch in enumerate(perm):
                mapping[chr(i + 97)] = ch

            remappedSignals = [convertSignal(signal, mapping) for signal in SIGNALS]
            remappedSignals = ["".join(sorted(signal)) for signal in remappedSignals]
            if validPermutation(signalsIn, remappedSignals):
                output = 0
                for signal in signalsOut:
                    output = 10 * output + getDigit(signal, remappedSignals)
                answer += output
                break

    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]

        print(filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 08"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
