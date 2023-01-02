from collections import namedtuple
from pathlib import Path


Point = namedtuple('Point', ['x', 'y'])


def task(knots_len=2):
    motions = [li.split(" ") for li in Path("day9_in.txt").read_text().splitlines()]

    knots = [Point(0, 0) for _ in range(knots_len)]
    visited = set()
    # print(f"Head: {head.x} - {head.y} | Tail: {tail.x} - {tail.y}")
    for direction, steps in motions:
        # print(f" {direction} - {steps}")
        for _ in range(int(steps)):
            # Head
            if direction == 'D':
                knots[0] = Point(knots[0].x, knots[0].y - 1)
            elif direction == 'U':
                knots[0] = Point(knots[0].x, knots[0].y + 1)
            elif direction == 'L':
                knots[0] = Point(knots[0].x - 1, knots[0].y)
            elif direction == 'R':
                knots[0] = Point(knots[0].x + 1, knots[0].y)

            for i in range(1, len(knots)):
                if abs(knots[i].x - knots[i-1].x) > 1:
                    if knots[i-1].x > knots[i].x:
                        knots[i] = Point(knots[i].x + 1, knots[i].y)
                    else:
                        knots[i] = Point(knots[i].x - 1, knots[i].y)

                    if abs(knots[i].y - knots[i-1].y) > 0:
                        if knots[i-1].y > knots[i].y:
                            knots[i] = Point(knots[i].x, knots[i].y + 1)
                        else:
                            knots[i] = Point(knots[i].x, knots[i].y - 1)

                elif abs(knots[i].y - knots[i-1].y) > 1:
                    if knots[i-1].y > knots[i].y:
                        knots[i] = Point(knots[i].x, knots[i].y + 1)
                    else:
                        knots[i] = Point(knots[i].x, knots[i].y - 1)
                    if abs(knots[i].x - knots[i-1].x) > 0:
                        if knots[i-1].x > knots[i].x:
                            knots[i] = Point(knots[i].x + 1, knots[i].y)
                        else:
                            knots[i] = Point(knots[i].x - 1, knots[i].y)
            visited.add((knots[-1].x, knots[-1].y))

    print(f"done with {knots_len} knots: {len(visited)}")


if __name__ == '__main__':
    task(2)
    task(10)
    # print('---')
    # task_b()
    # 2405


    # That's not the right answer. Curiously, it's the right answer for someone else; you might be logged in to the wrong account or just unlucky.
    # In any case, you need to be using your puzzle input. If you're stuck, make sure you're using the full input data;
    # there are also some general tips on the about page, or you can ask for hints on the subreddit.
    # Because you have guessed incorrectly 5 times on this puzzle, please wait 5 minutes before trying again. (You guessed 2449.)