import os
from collections import defaultdict


def get_input() -> tuple[list[str], list[str]]:
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_05")) as f:
        all_lines = f.read().splitlines()
        arrangement = all_lines[: all_lines.index("")]
        steps = all_lines[all_lines.index("") + 1 :]
        return (arrangement, steps)


def arrangement_to_stacks(arrangement: list[str]) -> dict[int, list[str]]:
    # Discard the line of numbers
    columns = defaultdict(list)
    arrangement.pop()
    while arrangement:
        cur_line = arrangement.pop()
        for i in range(1, 10):
            result, cur_line = cur_line[:4], cur_line[4:]
            letter = [*result][1]
            if letter != " ":
                columns[i].append(letter)
    return dict(columns)


def part_01(arrangement: list[str], steps: list[str]) -> str:
    stacks = arrangement_to_stacks(arrangement)
    for step in steps:
        step = step.split(" ")
        number = int(step[1])
        source = int(step[3])
        dest = int(step[5])

        for _ in range(number):
            stacks[dest].append(stacks[source].pop())

    return "".join([stacks[i][-1] for i in range(1, 10)])


def part_02(arrangement: list[str], steps: list[str]) -> str:
    stacks = arrangement_to_stacks(arrangement)
    for step in steps:
        step = step.split(" ")
        number = int(step[1])
        source = int(step[3])
        dest = int(step[5])

        moving, stacks[source] = stacks[source][-number:], stacks[source][:-number]

        stacks[dest].extend(moving)

    return "".join([stacks[i][-1] for i in range(1, 10)])


if __name__ == "__main__":
    arrangement, steps = get_input()
    print(f"Part 1: Score is {part_01(arrangement.copy(), steps)}.")
    print(f"Part 2: Score is {part_02(arrangement.copy(), steps)}.")
