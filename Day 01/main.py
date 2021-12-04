# https://adventofcode.com/2021/day/1


def getLargerMeasurments(data):
    return sum([1 if data[i] > data[i - 1] else 0 for i in range(1, len(data))])


def solvePart1(data):
    with open("Day 01/outputPart1.txt", "w") as file:
        file.write(str(getLargerMeasurments(data)))


def solvePart2(data):
    partialSum = [data[i - 2] + data[i - 1] + data[i] for i in range(2, len(data))]
    with open("Day 01/outputPart2.txt", "w") as file:
        file.write(str(getLargerMeasurments(partialSum)))


def main():
    data = None
    with open("Day 01/input.txt", "r") as file:
        data = [int(num.strip()) for num in file.readlines()]

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
