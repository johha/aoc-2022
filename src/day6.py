from pathlib import Path


def task(slice_len: int = 4):
    input = Path("day6_in.txt").read_text().splitlines()
    input = list(input[0])

    for i in range(0, len(input)-slice_len):
        if len(set(input[i:i+slice_len])) == slice_len:
            print(f"done: {i+slice_len}")
            break

if __name__ == '__main__':
    print("task a")
    task(4)
    print("task b")
    task(14)