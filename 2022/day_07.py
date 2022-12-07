import os
from functools import reduce
from collections import defaultdict
import operator

def part_01() -> int:
    # tree = lambda: defaultdict(tree)
    # root_filesystem = {"/": defaultdict(tree)}
    directory_tracker = ["/"]
    directory_cumulative_size = {}

    # Populate the directory tree as a dict
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_07")) as f:
        for line in f.read().splitlines():
            if line == "$ ls":
                # don't care about ls command, its always current dir
                pass
            elif line == "$ cd ..":
                directory_tracker.pop()
            elif line == "$ cd /":
                directory_tracker = ["/"]
            elif line.startswith("$ cd"):
                directory_tracker.append(line.split(" ")[2])  
            elif line.startswith("dir"):
                # don't care about dirs
                pass
            elif line[0].isdigit():
                filesize, name = line.split(" ")
                # reduce(operator.getitem, directory_tracker[:-1], root_filesystem)[directory_tracker[-1]][name] = int(filesize)
                
            
                for i in range(len(directory_tracker) +1):
                    merged_dir_key = "/".join(directory_tracker[:i])
                    directory_cumulative_size[merged_dir_key] = directory_cumulative_size.get(merged_dir_key, 0) + int(filesize)
                #print(directory_cumulative_size)
                
                
                
    # Calculate dir sizes
    sum = 0
    for dir in directory_cumulative_size:
        if directory_cumulative_size[dir] <= 100_000:
            sum += directory_cumulative_size[dir]
    return sum, directory_cumulative_size


def part_02(dirs: dict[str, int]) -> int:
    total_size = 70_000_000
    needed_size = 30_000_000
    used_size = dirs["/"]
    free_size = total_size - used_size
    need_to_free_size = needed_size-free_size
    size = 1000000000
    for dir in dirs:
        if dirs[dir] >= need_to_free_size:
            if dirs[dir] < size:

                size = dirs[dir]
    return size

if __name__ == "__main__":
    sum, dirs = part_01()
    print(f"Part 1: Total size of directories smaller than 100,000: {sum}.")
    print(f"Part 2: Size of the smallest directory we can remove is {part_02(dirs)}.")
