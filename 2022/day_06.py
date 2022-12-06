import os


def part_01() -> int:
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_06")) as f:
        for line in f.read().splitlines():
            # only one line
            input_str_list = [*line]
    count = 1
    char_set: set[str] = {}
    while len(char_set) != 4:
        char_set = {x for x in input_str_list[count : count + 4]}
        count += 1

    return count + 3


def part_02() -> int:
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_06")) as f:
        for line in f.read().splitlines():
            # only one line
            input_str_list = [*line]
    count = 1
    char_set: set[str] = {}
    while len(char_set) != 14:
        char_set = {x for x in input_str_list[count : count + 14]}
        count += 1

    return count + 13


if __name__ == "__main__":
    print(f"Part 1: Start of packet marker is {part_01()}.")
    print(f"Part 2: Start of packet marker is {part_02()}.")
