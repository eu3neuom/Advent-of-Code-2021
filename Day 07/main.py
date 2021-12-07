# https://adventofcode.com/2021/day/7


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
    with open("Day 07/outputPart1.txt", "w") as file:
        file.write(str(answer))


def solvePart2(data):
    answer = getMinCost(data, lambda x: int(x * (x + 1) / 2))
    with open("Day 07/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    data = None
    with open("Day 07/example.txt", "r") as file:
        data = [int(num) for num in file.readline().split(",")]

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
