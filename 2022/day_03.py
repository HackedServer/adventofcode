import os


priority = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def part_01():
    score = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_03")) as f:
        for line in f.read().splitlines():
            line_lenth = len(line)
            half1 = set(line[: int(line_lenth / 2)])
            half2 = set(line[int(line_lenth / 2) :])

            similar_character = half1 & half2
            similar_character = similar_character.pop()
            score += priority.index(similar_character) + 1
    return score


def part_02():
    score = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_03")) as f:
        inputs = f.read().splitlines()
        while inputs:
            one = set(inputs.pop())
            two = set(inputs.pop())
            three = set(inputs.pop())

            similar_character = one & two & three
            similar_character = similar_character.pop()
            score += priority.index(similar_character) + 1
            print(similar_character)
    return score


if __name__ == "__main__":
    print(f"Part 1: Score is {part_01()}.")
    print(f"Part 2: Score is {part_02()}.")
