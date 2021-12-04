# https://adventofcode.com/2021/day/1


def getFrequency(data):
    frequency = [0] * len(data[0])
    for line in data:
        for i, char in enumerate(line):
            frequency[i] += int(char == "1")

    return frequency


def solvePart1(data):
    frequency = getFrequency(data)
    frequency.reverse()

    gamma = epsilon = 0
    for i, occurences in enumerate(frequency):
        if occurences > len(data) - occurences:
            gamma += 1 << i
        else:
            epsilon += 1 << i

    answer = gamma * epsilon
    with open("Day 03/outputPart1.txt", "w") as file:
        file.write(str(answer))


def removeDiagnostic(data, position, bitValue):
    return [x for x in data if int(x[position]) != bitValue]


def getGasRating(data, specialBit):
    gas = data
    for i in range(len(gas[0])):
        if len(gas) == 1:
            break
        frequency = getFrequency(gas)
        if frequency[i] >= len(gas) - frequency[i]:
            gas = removeDiagnostic(gas, i, specialBit)
        else:
            gas = removeDiagnostic(gas, i, 1 - specialBit)

    return int(gas[0], 2)


def solvePart2(data):
    OXIGEN_SPECIAL_BIT = 0
    CO2_SPECIAL_BIT = 1

    oxygen = getGasRating(data, OXIGEN_SPECIAL_BIT)
    co2 = getGasRating(data, CO2_SPECIAL_BIT)
    answer = oxygen * co2
    with open("Day 03/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    data = None
    with open("Day 03/input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
