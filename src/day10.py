import math
from pathlib import Path


def task_a():

    program = [li.split(" ") for li in Path("day10_in.txt").read_text().splitlines()]

    instruction_counter = 0
    val_X = 1

    signals = []

    wait_counter = 0
    addX = False

    for i in range(1, 221):
        if i in (20, 60, 100, 140, 180, 220):
            signals.append(val_X * i)
        if wait_counter > 0:
            wait_counter -= 1

        if wait_counter == 0 and addX:
            addX = False
            val_X += int(program[instruction_counter][1])
            instruction_counter += 1
        elif program[instruction_counter][0] == "noop":
            instruction_counter += 1
            continue
        elif program[instruction_counter][0] == "addx":
            addX = True
            wait_counter += 1 # two cycle to complete

    print(f"done: {sum(signals)}")


def task_b():

    program = [li.split(" ") for li in Path("day10_in.txt").read_text().splitlines()]

    instruction_counter = 0
    val_X = 1


    wait_counter = 0
    addX = False

    sprite_pos = 0


    for i in range(240):
        if i % 40 == 0:
            print("")

        crt_pos = i % 40
        if crt_pos in range(sprite_pos, sprite_pos + 3):
            print('#', end="")
        else:
            print(".", end="")

        if wait_counter > 0:
            wait_counter -= 1

        if wait_counter == 0 and addX:
            addX = False
            val_X += int(program[instruction_counter][1])
            instruction_counter += 1

            sprite_pos = val_X - 1

        elif program[instruction_counter][0] == "noop":
            instruction_counter += 1
            continue
        elif program[instruction_counter][0] == "addx":
            addX = True
            wait_counter += 1  # two cycle to complete

    # print(f"done: {sum(signals)}")


if __name__ == '__main__':
    # task_a()
    task_b()