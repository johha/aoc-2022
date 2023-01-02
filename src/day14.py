import itertools
import math
from collections import namedtuple
from pathlib import Path


def task(with_floor = False):
    paths = [p.split("->") for p in Path("day14_in.txt").read_text().splitlines()]
    paths = [[c.split(",") for c in p] for p in paths]
    paths = [[list(map(int, c)) for c in p] for p in paths]


    x_min = min([xy[0] for xy in list(itertools.chain.from_iterable(paths))])
    x_max = max([xy[0] for xy in list(itertools.chain.from_iterable(paths))])
    y_max = max([xy[1] for xy in list(itertools.chain.from_iterable(paths))])

    cave = [["." for _ in range(0, 1000)] for _ in range(0, y_max + 1)]

    if with_floor:
        cave.append(["." for _ in range(0, x_max * 2)])
        cave.append(["#" for _ in range(0, x_max * 2)])

    for p in paths:
        for p1, p2 in itertools.pairwise(p):
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                cave[p1[1]][x] = '#'
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                cave[y][p1[0]] = '#'

    Point = namedtuple('Point', ['x', 'y'])

    filling_point = Point(500, 0)
    cave[filling_point[1]][filling_point[0]] = "+"


    sand_grains = 0
    filled = False

    while True:
        current_pos = filling_point
        while True:
            if current_pos.y not in range(0, len(cave) - 1) or current_pos.x not in range(0, len(cave[1]) - 1):
                filled = True
                break
            elif cave[current_pos.y + 1][current_pos.x] == ".":
                current_pos = Point(x=current_pos.x, y=current_pos.y + 1)
                continue
            elif cave[current_pos.y + 1][current_pos.x - 1] == ".":
                current_pos = Point(x=current_pos.x - 1, y=current_pos.y + 1)
                continue
            elif cave[current_pos.y + 1][current_pos.x + 1] == ".":
                current_pos = Point(x=current_pos.x + 1, y=current_pos.y + 1)
                continue
            else:
                cave[current_pos.y][current_pos.x] = "o"
                sand_grains += 1
                # print(f"{current_pos.x} - {current_pos.x}")
                if current_pos == filling_point:
                    filled = True
                break
        if filled:
            break



    # for row in cave:
    #     for x in row:
    #         print(x, end="")
    #     print()

    print(f"done: {sand_grains}")




if __name__ == '__main__':
    print("task a")
    task()

    print("task b")
    task(with_floor=True)