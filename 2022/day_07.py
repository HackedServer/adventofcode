import os


def compute_directory_sizes() -> dict[str, int]:
    directory_tracker = ["/"]
    directory_cumulative_size = {}

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_07")) as f:
        for line in f.read().splitlines():
            if line == "$ cd ..":
                directory_tracker.pop()
            elif line == "$ cd /":
                directory_tracker = ["/"]
            elif line.startswith("$ cd"):
                directory_tracker.append(line.split(" ")[2])
            elif line[0].isdigit():
                filesize = int(line.split(" ")[0])
                for i in range(len(directory_tracker) + 1):
                    merged_dir_key = tuple(directory_tracker[:i])
                    directory_cumulative_size[merged_dir_key] = (
                        directory_cumulative_size.get(merged_dir_key, 0) + filesize
                    )

    return directory_cumulative_size


def part_01(directory_sizes: dict[str, int]) -> int:
    sum = 0
    for dir in directory_sizes:
        if directory_sizes[dir] <= 100_000:
            sum += directory_sizes[dir]

    return sum


def part_02(dirs: dict[str, int]) -> int:
    total_size = 70_000_000
    needed_size = 30_000_000
    used_size = dirs[tuple("/")]
    free_size = total_size - used_size
    need_to_free_size = needed_size - free_size
    size = float('inf')
    for dir in dirs:
        if dirs[dir] >= need_to_free_size and dirs[dir] < size:
            size = dirs[dir]
    return int(size)


if __name__ == "__main__":
    dirs = compute_directory_sizes()
    print(f"Part 1: Total size of directories smaller than 100,000: {part_01(dirs)}.")
    print(f"Part 2: Size of the smallest directory we can remove is {part_02(dirs)}.")
