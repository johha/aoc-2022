import re
from pathlib import Path

def possible(x, y, sensors, beacons):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True

def task(target_line=10):
    sensors, beacons, sensors_pos = set(), set(), set()
    for line in Path("day15_example.txt").read_text().splitlines():
        sensor, beacon = line.split(":", 1)
        sx, sy = map(int, re.findall('-?\d+', sensor))
        bx, by = map(int, re.findall('-?\d+', beacon))
        distance = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, distance))
        sensors_pos.add((sx, sy))
        beacons.add((bx, by))

    no_beacon_pos = set()
    min_x = min(x - d for x, _, d in sensors)
    max_x = max(x + d for x, _, d in sensors)
    y = target_line
    for x in range(min_x, max_x):
        if (x, y) in beacons:
            continue
        for sx, sy, d in sensors:
            if abs(x - sx) + abs(y - sy) <= d:
                no_beacon_pos.add((x, y))
                break

    print(f"Positions without beacon: {len(no_beacon_pos)}")


    multiplier = 4_000_000

    pos_min, pos_max = 0, 20
    free_pos = set()


    done = False
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                print(f"sx: {sx}, sy: {sy}, dx: {dx}, dy: {dy}, x: {x}, y: {y}")
                if not(x <= pos_max and 0<=y<=pos_max):
                    continue
                if possible(x, y, sensors, beacons):
                    done = True
                    break
            if done:
                break
        if done:
            break
    print(x * multiplier + y)


    # for y in range(pos_min, pos_max + 1):
    #     for x in range(pos_min, pos_max):
    #         if (x, y) in beacons or (x, y) in no_beacon_pos:
    #             continue
    #         free = True
    #         for sx, sy, d in sensors:
    #             if abs(x - sx) + abs(y - sy) <= d:
    #                 free = False
    #                 break
    #         if free:
    #             free_pos.add((x, y))
    free_pos = list(free_pos)
    print(f"Distress beacon at: {free_pos[0][0] * multiplier + free_pos[0][1]}")


if __name__ == '__main__':
    # task(10)
    task(2000000)
