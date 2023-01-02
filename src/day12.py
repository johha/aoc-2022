from pathlib import Path
from collections import deque


def task():
    map = [list(m) for m in Path("day12_in.txt").read_text().splitlines()]

    starts = []
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "S":
                starts.append((x, y))
                start = (x, y)
                map[y][x] = ord("a")
            elif c == "E":
                target = (x, y)
                map[y][x] = ord("z")
            else:
                if c == "a":
                    starts.append((x, y))
                map[y][x] = ord(c)

    assert start
    assert target

    paths = []

    for s in starts:

        visited = {s}
        todo = deque([(s, 0)])
        while todo:
            (cx, cy), d = todo.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = cx + dx, cy + dy
                if (
                        0 <= nx < len(map[0])
                        and 0 <= ny < len(map)
                        and (nx, ny) not in visited
                        and map[ny][nx] <= map[cy][cx] + 1
                ):
                    if (nx, ny) == target:
                        paths.append(d+1)
                        break
                    todo.append(((nx, ny), d + 1))
                    visited.add((nx, ny))

    print(min(paths))

if __name__ == '__main__':
    task()