# https://adventofcode.com/2021/day/4


class Board:
    def __init__(self):
        self.rows = [0] * 5
        self.columns = [0] * 5
        self.numbers = {}
        self.answer = None
        self.won = False
        self.order = 0

    def build(self, data):
        if len(data) != 6:
            return False

        for i in range(5):
            line = [int(x) for x in data[i].strip().split()]
            for j in range(5):
                self.numbers[line[j]] = (i, j, False)
        return True

    def sumUnmarked(self):
        unmarked = 0
        for number, (_, _, used) in self.numbers.items():
            if not used:
                unmarked += number
        return unmarked


def playBingo(extractedNumbers, boards):
    winId = 0
    for number in extractedNumbers:
        for board in boards:
            if board.won:
                continue
            if number in board.numbers.keys():
                x, y, _ = board.numbers[number]
                board.rows[x] += 1
                board.columns[y] += 1
                board.numbers[number] = (x, y, True)

                if board.rows[x] == 5 or board.columns[y] == 5:
                    board.won = True
                    board.order = winId
                    board.answer = board.sumUnmarked() * number
                    winId += 1


def answerForBoardWithOrder(boards, order):
    for board in boards:
        if board.order == order:
            return board.answer


def solvePart1(extractedNumbers, boards):
    playBingo(extractedNumbers, boards)
    answer = answerForBoardWithOrder(boards, 0)
    with open("Day 04/outputPart1.txt", "w") as file:
        file.write(str(answer))


def solvePart2(extractedNumbers, boards):
    playBingo(extractedNumbers, boards)
    answer = answerForBoardWithOrder(boards, len(boards) - 1)
    with open("Day 04/outputPart2.txt", "w") as file:
        file.write(str(answer))


def main():
    extractedNumbers = None
    boards = []
    with open("Day 04/input.txt", "r") as file:
        extractedNumbers = [int(x) for x in file.readline().strip().split(",")]
        file.readline()
        data = file.readlines()
        for i in range(6, len(data) + 1, 6):
            board = Board()
            board.build(data[i - 6 : i])
            boards.append(board)

    solvePart1(extractedNumbers, boards)
    solvePart2(extractedNumbers, boards)


if __name__ == "__main__":
    main()
