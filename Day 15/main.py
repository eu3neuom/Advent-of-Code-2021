# https://adventofcode.com/2021/day/15
import os
from heapq import heappush, heappop

DX = [-1, 0, 1, 0]
DY = [0, -1, 0, 1]


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, element):
        heappush(self.heap, element)

    def getMin(self):
        return heappop(self.heap)

    def empty(self):
        return len(self.heap) == 0


def BFS(matrix):
    global DX, DY

    n = len(matrix)
    m = len(matrix[0])
    dp = [[1000 ** 5 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0

    heap = Heap()
    heap.push((0, 0, 0))
    while not heap.empty():
        dist, x, y = heap.getMin()
        if dp[x][y] != dist:
            continue
        for dir in range(len(DX)):
            nx = x + DX[dir]
            ny = y + DY[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist + matrix[nx][ny] < dp[nx][ny]:
                dp[nx][ny] = dist + matrix[nx][ny]
                heap.push((dp[nx][ny], nx, ny))
    return dp[n - 1][m - 1]


def solvePart1(matrix):
    answer = BFS(matrix)
    print("└─Part 01: ", answer)


def expand(matrix):
    n = len(matrix)
    m = len(matrix[0])
    newMatrix = [[0 for _ in range(m * 5)] for _ in range(n * 5)]
    for i in range(n * 5):
        for j in range(m * 5):
            prev = matrix[i % n][j % m]
            add = (i // n) + (j // m)
            newMatrix[i][j] = prev + add
            while newMatrix[i][j] > 9:
                newMatrix[i][j] -= 9
    return newMatrix


def solvePart2(matrix):
    answer = BFS(expand(matrix))
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip() for line in file.readlines()]
        matrix = [[int(x) for x in line] for line in data]

        print("For " + filePath)
        solvePart1(matrix)
        solvePart2(matrix)


if __name__ == "__main__":
    DAY_PATH = "Day 15"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
