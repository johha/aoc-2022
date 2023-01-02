import copy
import itertools
from pathlib import Path


def task():
    input_stacks, instructions = [cnt.splitlines() for cnt in Path("day5_in.txt").read_text().split("\n\n")]

    input_stacks = [list(s.replace('   ', 'X').replace('[', '').replace(' ', '').replace(']', '')) for s in input_stacks]
    num_stacks = int(list(input_stacks[-1])[-1])

    # stacks = list(itertools.zip_longest(*input_stacks[:-1]))
    stacks_a = []
    for k in range(0, num_stacks):
        s = []
        for l in range(len(input_stacks[:-1]), 0, -1):
            try:
                value = input_stacks[l-1][k]
                if value != "X":
                    s.append(value)
            except IndexError:
                continue
        stacks_a.append(s)
    stacks_b = copy.deepcopy(stacks_a)

    # move;from;to
    instructions = [[*map(int, i.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))] for i in instructions]

    for i in instructions:
        for move in range(i[0]):
            # task a
            e = stacks_a[i[1] - 1].pop()
            stacks_a[i[2] - 1].append(e)

        # task b
    for i in instructions:
        index = -1 * i[0]
        stacks_b[i[2] - 1].extend(stacks_b[i[1] - 1][index:])
        stacks_b[i[1] - 1] = stacks_b[i[1] - 1][:index]


    print("task a")
    print()
    [print(s[-1], end='') for s in stacks_a]
    print()
    print("task b")
    print()
    [print(s[-1], end='') for s in stacks_b]
    print()
    print("done")
    #
if __name__ == '__main__':
    task()