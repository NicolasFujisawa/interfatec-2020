from itertools import combinations


def is_possible_sum(numbers, n):
    for r in range(len(numbers)):
        for combo in combinations(numbers, r + 1):
            if sum(combo) == n:
                return "SIM"
    return "NAO"


def solution():
    [target, qtd] = [int(value) for value in input().split(" ")]
    pecas = [int(value) for value in input().split(" ")]

    print(is_possible_sum(pecas, target))


solution()
