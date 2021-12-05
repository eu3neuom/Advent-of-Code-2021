# https://adventofcode.com/2021/day/5

from collections import Counter


def getPoints(pair, useDiagonals):
    bx, by, ex, ey = pair
    if not useDiagonals and (bx != ex and by != ey):
        return []

    points = [bx * 100000 + by]
    while bx != ex or by != ey:
        if bx != ex:
            bx += 1 if bx < ex else -1
        if by != ey:
            by += 1 if by < ey else -1
        points.append(bx * 100000 + by)
    return points


def getAnswer(points):
    counter = Counter()
    counter.update(points)

    answer = 0
    for x in counter:
        answer += 1 if counter[x] > 1 else 0
    return answer


def solvePart1(data):
    points = []
    for pair in data:
        points += getPoints(pair, False)

    answer = getAnswer(points)
    with open("Day 05/outputPart1.txt", "w") as file:
        file.write(str(answer))


def solvePart2(data):
    points = []
    for pair in data:
        points += getPoints(pair, True)

    answer = getAnswer(points)
    with open("Day 05/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    data = []
    with open("Day 05/input.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            data.append([int(x) for x in (line[0] + "," + line[2]).split(",")])

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
