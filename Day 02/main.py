# https://adventofcode.com/2021/day/2


def normalizeCommand(command, units):
    switcher = {"forward": [units, 0], "down": [0, units], "up": [0, -units]}
    return switcher[command]


def solvePart1(data):
    # Horizontal, Depth
    coords = [0, 0]
    for command, units in data:
        move = normalizeCommand(command, int(units))
        coords = [sum(x) for x in zip(coords, move)]

    answer = coords[0] * coords[1]
    with open("Day 02/outputPart1.txt", "w") as file:
        file.write(str(answer))


def solvePart2(data):
    # Horizontal, Aim, Depth
    coords = [0, 0, 0]
    for command, units in data:
        move = normalizeCommand(command, int(units))
        coords = [
            coords[0] + move[0],
            coords[1] + move[1],
            coords[2] + coords[1] * move[0],
        ]

    answer = coords[0] * coords[2]
    with open("Day 02/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    data = None
    with open("Day 02/input.txt", "r") as file:
        data = [line.strip().split() for line in file.readlines()]

    solvePart1(data)
    solvePart2(data)


if __name__ == "__main__":
    main()
