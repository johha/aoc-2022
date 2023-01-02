import math
from pathlib import Path

def task_a():
    tree_map = [list(map(int, li)) for li in Path("day8_in.txt").read_text().splitlines()]

    visible_tree = set()
    vmap = [[0] * (len(tree_map[0])) for _ in range(len(tree_map))]

    for y, row in enumerate(tree_map):
        for x, height in enumerate(row):
            if x == 0 or x == len(row) - 1:
                visible_tree.add((y, x, height))
                vmap[y][x] = 'V'
            elif y == 0 and x >= 1:
                visible_tree.add((y, x, height))
                vmap[y][x] = 'V'
            elif y == len(tree_map) - 1 and x >= 1:
                visible_tree.add((y, x, height))
                vmap[y][x] = 'V'

            # Not on the edge
            else:
                visible = False
                # Left row
                for left_x in range(x-1, -1, -1):
                    left_height = row[left_x]
                    if left_height >= height:
                        visible = False
                        break
                    visible = True
                if visible:
                    visible_tree.add((x, y, height))
                    vmap[y][x] = 'V'
                    continue

                # Right row
                for right_x in range(x+1, len(row)):
                    right_height = row[right_x]
                    if right_height >= height:
                        visible = False
                        break
                    visible = True
                if visible:
                    visible_tree.add((x, y, height))
                    vmap[y][x] = 'V'
                    continue

                # Up
                for up_y in range(y - 1, -1, -1):
                    if tree_map[up_y][x] >= height:
                        visible = False
                        break
                    visible = True
                if visible:
                    visible_tree.add((x, y, height))
                    vmap[y][x] = 'V'
                    continue

                # Down
                for down_y in range(y + 1, len(tree_map)):
                    if tree_map[down_y][x] >= height:
                        visible = False
                        break
                    visible = True
                if visible:
                    visible_tree.add((x, y, height))
                    vmap[y][x] = 'V'
                    continue






    print(f"done: {len(visible_tree)}")

    # print()
    #
    # for y, row in enumerate(vmap):
    #     for x in row:
    #         print(x, end='')
    #     print()


def task_b():
    tree_map = [list(map(int, li)) for li in Path("day8_in.txt").read_text().splitlines()]

    total_score = []
    # vmap = [[0] * (len(tree_map[0])) for _ in range(len(tree_map))]

    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[y]) - 1):
            height = tree_map[y][x]
            score = []

            # Left row
            counter = 0
            for left_x in range(x-1, -1, -1):
                local_height = tree_map[y][left_x]
                if local_height < height:
                    counter += 1
                    continue
                elif local_height >= height:
                    counter += 1
                    break
            score.append(counter)

            # Right row
            counter = 0
            for right_x in range(x+1, len(tree_map[y])):
                local_height = tree_map[y][right_x]
                if local_height < height:
                    counter += 1
                    continue
                elif local_height >= height:
                    counter += 1
                    break
            score.append(counter)

            # Up
            counter = 0
            for up_y in range(y - 1, -1, -1):
                local_height = tree_map[up_y][x]
                if local_height < height:
                    counter += 1
                    continue
                elif local_height >= height:
                    counter += 1
                    break
            score.append(counter)

            # Down
            counter = 0
            for down_y in range(y + 1, len(tree_map)):
                local_height = tree_map[down_y][x]
                if local_height < height:
                    counter += 1
                    continue
                elif local_height >= height:
                    counter += 1
                    break
            score.append(counter)

            total_score.append(math.prod(score))





    print(f"done: {sorted(total_score, reverse=True)[0]}")

if __name__ == '__main__':
    task_b()
