import operator
from pathlib import Path
from typing import List, Dict


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Dir():
    def __init__(self, name: str, parent: "Dir" = None):
        self.name = name
        self.files = {}
        self.sub_dirs = {}
        self.parent = parent

    def add_file(self, name: str, size: int):
        self.files[name] = size

    def add_sub_dir(self, name: str):
        self.sub_dirs[name] = (Dir(name=name, parent=self))

    def get_size(self) -> int:
        size = 0
        for f in self.files.values():
            size += int(f)
        for d in self.sub_dirs.values():
            size += d.get_size()
        return size

    def task_a(self) -> int:
        size = 0
        tmp_size = self.get_size()
        if tmp_size <= 100000:
            size += tmp_size
        for d in self.sub_dirs.values():
            size += d.task_a()
        return size

    def task_b(self, size_needed) -> int:
        dirs = {}
        tmp_size = self.get_size()
        if tmp_size >= size_needed:
            dirs[self.name] = tmp_size
        for d in self.sub_dirs.values():
            dirs.update(d.task_b(size_needed))
        return dirs

def task():
    input = Path("day7_in.txt").read_text().splitlines()

    cwd = None
    root = None

    for i, val in enumerate(input):
        # Change dir
        if val.startswith("$ cd"):
            if val.endswith("/") and i == 0:
                root = Dir(name="/")
                cwd = root
            elif val.endswith('..'):
                cwd = cwd.parent
            else:
                target_dir = val.split(" ")[2]
                cwd = cwd.sub_dirs[target_dir]
        # List
        elif val == "$ ls":
            pass
        elif val.startswith("dir"):
            cwd.add_sub_dir(val.split(" ")[1])
        # Files
        else:
            size, name = val.split(" ")
            cwd.add_file(name, size)

    print(f"done: {root.task_a()}")
    used = root.get_size()
    unused = 70000000 - used

    for_update = 30000000 - unused

    print(for_update)
    dirs = root.task_b(for_update)
    print(sorted(dirs.items(), key=operator.itemgetter(1)))



if __name__ == '__main__':
    task()
