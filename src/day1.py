from pathlib import Path
def task():
    data = Path("day1_in.txt").read_text().split("\n\n")
    data = [[int(item) for item in pack.splitlines()] for pack in data]
    data = [sum(pack) for pack in data]
    data = sorted(data)

    print("task a")
    print(data[-1])
    print("task b")
    print(sum(data[-3:]))


if __name__ == '__main__':
    task()