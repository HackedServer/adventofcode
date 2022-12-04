import os


def part_01():
    pairs = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_04")) as f:
        for line in f.read().splitlines():
            one, two = line.split(",")
            one_range = [*range(int(one.split("-")[0]), 1 + int(one.split("-")[1]))]
            two_range = [*range(int(two.split("-")[0]), 1 + int(two.split("-")[1]))]
            if all(x in two_range for x in one_range):
                pairs += 1
            elif all(x in one_range for x in two_range):
                pairs += 1
    return pairs


def part_02():
    pairs = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_04")) as f:
        for line in f.read().splitlines():
            one, two = line.split(",")
            one_range = [*range(int(one.split("-")[0]), 1 + int(one.split("-")[1]))]
            two_range = [*range(int(two.split("-")[0]), 1 + int(two.split("-")[1]))]
            if any(x in two_range for x in one_range):
                pairs += 1
            elif any(x in one_range for x in two_range):
                pairs += 1
    return pairs


if __name__ == "__main__":
    print(f"Part 1: Score is {part_01()}.")
    print(f"Part 2: Score is {part_02()}.")
