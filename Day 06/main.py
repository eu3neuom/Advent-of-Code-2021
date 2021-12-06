# https://adventofcode.com/2021/day/6


def solve(daysNumber, data):
    frequency = [0] * 11
    for num in data:
        frequency[num] += 1

    for i in range(daysNumber):
        zeros = frequency[0]
        for j in range(10):
            frequency[j] = frequency[j + 1]
        frequency[8] += zeros
        frequency[6] += zeros
        answer = sum(frequency)
    return answer


def solvePart1(data):
    answer = solve(80, data)
    with open("Day 06/outputPart1.txt", "w") as file:
        file.write(str(answer))


def solvePart2(data):
    answer = solve(256, data)
    with open("Day 06/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    data = None
    with open("Day 06/input.txt", "r") as file:
        data = [int(num) for num in file.readline().split(",")]

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
