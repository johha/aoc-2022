import math
from pathlib import Path


def task(rounds=20, relief=True):
    monkey_in = [m.splitlines() for m in Path("day11_in_test.txt").read_text().split("\n\n")]

    monkeys = {}
    modulo = 1

    for m in monkey_in:
        m_key = 0
        for attr in m:
            if attr.startswith("Monkey"):
                m_key = attr.split(" ")[1].split(":")[0]
                monkeys[m_key] = {}
                monkeys[m_key]["inspect_counter"] = 0
            elif attr.startswith("  Starting items"):
                items = list(map(int, attr.split(":")[1].split(",")))
                monkeys[m_key]['items'] = items
            elif attr.startswith("  Operation"):
                ops = attr.split("=")[1].split(" ")[1:]
                monkeys[m_key]['operation'] = {'val1': ops[0], 'op': ops[1], 'val2': ops[2]}
            elif attr.startswith("  Test: divisible by"):
                monkeys[m_key]["test"] = int(attr.split("by ")[-1])
                modulo *= monkeys[m_key]["test"]
            elif attr.startswith("    If true:"):
                monkeys[m_key]["true_throw"] = int(attr.split(" ")[-1])
            elif attr.startswith("    If false:"):
                monkeys[m_key]["false_throw"] = int(attr.split(" ")[-1])


    for r in range(rounds):
        if r % 100 == 0:
            print(r)
        for i, vals in monkeys.items():
            for worry_level in vals["items"]:
                vals["inspect_counter"] += 1
                v1 = worry_level if vals["operation"]["val1"] == "old" else int(vals["operation"]["val1"])
                v2 = worry_level if vals["operation"]["val2"] == "old" else int(vals["operation"]["val2"])

                new_worry_level = 0
                if vals["operation"]["op"] == "*":
                    new_worry_level = v1 * v2
                elif vals["operation"]["op"] == "+":
                    new_worry_level = v1 + v2
                if relief:
                    new_worry_level = int(new_worry_level / 3)

                tmp = new_worry_level
                new_worry_level = new_worry_level % modulo  # Reduces value so that are numbers are smaller. With module it's still dividable

                if new_worry_level % vals["test"] == 0:
                    monkeys[str(vals["true_throw"])]["items"].append(new_worry_level)
                else:
                    monkeys[str(vals["false_throw"])]["items"].append(new_worry_level)

            monkeys[i]["items"] = []

    res = sorted([m["inspect_counter"] for m in monkeys.values()])
    print(f"done: {math.prod(res[-2:])}")

if __name__ == '__main__':
    task(20)
    print("---")
    task(10000, False)