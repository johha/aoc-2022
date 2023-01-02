from pathlib import Path


def range_fully_contains(x, y):
    return (x.start >= y.start and x.stop <= y.stop) or (y.start >= x.start and y.stop <= x.stop)


def overlaps(x, y):
    return (x.start <= y.start <= x.stop) or (y.start <= x.start <= y.stop)

def task(func):
    pairs = Path("day4_in.txt").read_text().splitlines()

    matches = 0
    for pair in pairs:
        p1, p2 = [p.split("-") for p in pair.split(",")]

        if func(range(int(p1[0]), int(p1[1])), range(int(p2[0]), int(p2[1]))):
            matches += 1

    return matches


if __name__ == '__main__':
    print(f"task a: {task(range_fully_contains)}")
    print(f"task b: {task(overlaps)}")
