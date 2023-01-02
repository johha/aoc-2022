import json
import math
import random
from functools import cmp_to_key
from json import JSONDecodeError
from pathlib import Path


def task_a():
    pairs = [l.splitlines() for l in Path("day13_in.txt").read_text().split("\n\n")]

    right_order_indices = []
    for i, p in enumerate(pairs):
        left = convert(p[0])
        right = convert(p[1])
        if determine_right_order(left, right) == -1:
           right_order_indices.append(i + 1)
    print(f"Part 1 - sum of order indices: {sum(right_order_indices)}")


def task_b():
    lines = sum([l.splitlines() for l in Path("day13_in.txt").read_text().split("\n\n")], [])
    lines = [convert(l) for l in lines] + [[[2]]] + [[[6]]]
    lines.sort(key=cmp_to_key(determine_right_order))

    divider_packets_indices = []

    for i, l in enumerate(lines):
        if l == [[2]] or l == [[6]]:
            divider_packets_indices.append(i+1)

    print(f"Part 2 - sum of divider indices: {math.prod(divider_packets_indices)}")

def convert(value):
    if isinstance(value, list) or isinstance(value, int):
        return value
    else:
        try:
            return json.loads(value)
        except (JSONDecodeError, TypeError):
            return int(value)
        except ValueError:
            print("this should not happen")
            raise


def determine_right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)

    elif isinstance(left, list) and isinstance(right, int):
        return determine_right_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return determine_right_order([left], right)

    for ll, rr in zip(left, right):
        if r := determine_right_order(ll, rr):
            return r
    return determine_right_order(len(left), len(right))





if __name__ == '__main__':
    # task_a()
    task_b()