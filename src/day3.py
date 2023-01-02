from enum import Enum
from pathlib import Path


def task_a():
    backpacks = Path("day3_in.txt").read_text().splitlines()

    score = 0
    for b in backpacks:
        b = list(b)
        same_values = set(b[:len(b)//2]) & set(b[len(b)//2:])
        assert len(same_values) == 1
        same_values = list(same_values)

        if same_values[0].islower():
            score += ord(same_values[0])-96
        else:
            score += ord(same_values[0])-64+26

    print(f"done: {score}")


def task_b():
    backpacks = Path("day3_in.txt").read_text().splitlines()
    groups = [backpacks[x:x+3] for x in range(0, len(backpacks), 3)]
    score = 0

    for g in groups:
        same_values = set(g[0]) & set(g[1]) & set(g[2])
        assert len(same_values) == 1
        same_values = list(same_values)

        if same_values[0].islower():
            score += ord(same_values[0])-96
        else:
            score += ord(same_values[0])-64+26

    print(f"done: {score}")

if __name__ == '__main__':
    task_b()
