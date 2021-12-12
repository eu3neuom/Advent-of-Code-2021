# https://adventofcode.com/2021/day/12
import os


def initialize(data):
    graph, marked = {}, {}
    for a, b in data:
        marked[a], marked[b] = 0, 0
        graph[a], graph[b] = [], []
    for a, b in data:
        graph[a].append(b)
        graph[b].append(a)
    return graph, marked


def smallMarkedTwice(marked):
    return sum(int(value == 2) for _, value in marked.items())


def DFS(graph, marked, node, allowTwice):
    if node == "end":
        return 1

    paths = 0
    marked[node] += 1 if node == node.lower() else 0
    for next in graph[node]:
        if next == "start" or (marked[next] and smallMarkedTwice(marked) == allowTwice):
            continue
        paths += DFS(graph, marked, next, allowTwice)
    marked[node] -= 1 if node == node.lower() else 0
    return paths


def solvePart1(data):
    graph, marked = initialize(data)
    answer = DFS(graph, marked, "start", 0)
    print("└─Part 01: ", answer)


def solvePart2(data):
    graph, marked = initialize(data)
    answer = DFS(graph, marked, "start", 1)
    print("└─Part 02: ", answer)


def solveProblem(filePath):
    with open(filePath, "r") as file:
        data = [line.strip().split("-") for line in file.readlines()]

        print("For " + filePath)
        solvePart1(data)
        solvePart2(data)


if __name__ == "__main__":
    DAY_PATH = "Day 12"
    solveProblem(os.path.join(DAY_PATH, "example.txt"))
    solveProblem(os.path.join(DAY_PATH, "input.txt"))
