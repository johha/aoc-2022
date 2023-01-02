from enum import Enum
from pathlib import Path


def score(p1, p2):
    if (p1 - 1) % 3 == p2:
        return p2 + 1
    elif (p2 - 1) % 3 == p1:
        return p2 + 7
    return p2 + 4


def sol():
    data = Path("day2_in.txt").read_text().splitlines()
    data = [line.split() for line in data]
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]

    moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in data]

    print(sum(score(p1, p2) for p1, p2 in data))
    print(sum(score(p1, p2) for p1, p2 in moves))

def task_a():
    rounds = Path("day2_in.txt").read_text().splitlines()

    total_score = 0

    for r in rounds:
        op_me = r.split(" ")
        op = op_me[0]
        me = op_me[1]

        winner = calc_winner(op, me)
        if winner == "me":
            total_score += 6
        if winner == "draw":
            total_score += 3
        if winner == "op":
            total_score += 0

        if me == "X":
            total_score += 1
        if me == "Y":
            total_score += 2
        if me == "Z":
            total_score += 3

    print(f"done: {total_score}")


def calc_winner(op: str, me: str) -> str:
    # Rock
    if op == 'A' and me == 'X':  # Rock
        return 'draw'
    if op == 'A' and me == 'Y':  # Paper
        return 'me'
    if op == 'A' and me == 'Z':  # Scissors
        return 'op'

    # Paper
    if op == 'B' and me == 'X':  # Rock
        return 'op'
    if op == 'B' and me == 'Y':  # Paper
        return 'draw'
    if op == 'B' and me == 'Z':  # Scissors
        return 'me'

    # Scissors
    if op == 'C' and me == 'X':  # Rock
        return 'me'
    if op == 'C' and me == 'Y':  # Paper
        return 'op'
    if op == 'C' and me == 'Z':  # Scissors
        return 'draw'


def task_b():
    rounds = Path("day2_in.txt").read_text().splitlines()

    total_score = 0

    for r in rounds:
        op_result = r.split(" ")
        op = op_result[0]
        result = op_result[1]

        shape = calc_shape(op, result)
        if result == "X":
            total_score += 0
        if result == "Y":
            total_score += 3
        if result == "Z":
            total_score += 6

        if shape == "A":
            total_score += 1
        if shape == "B":
            total_score += 2
        if shape == "C":
            total_score += 3

    print(f"done: {total_score}")


def calc_shape(op: str, result: str) -> str:
    if result == "Y":
        return op

    # lose
    if result == "X" and op == "A":
        return "C"
    if result == "X" and op == "B":
        return "A"
    if result == "X" and op == "C":
        return "B"

    # win
    if result == "Z" and op == "A":
        return "B"
    if result == "Z" and op == "B":
        return "C"
    if result == "Z" and op == "C":
        return "A"


if __name__ == '__main__':
    sol()
