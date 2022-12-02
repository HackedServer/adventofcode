import os

"""
A for Rock
B for Paper
C for Scissors

X for Rock
Y for Paper
Z for Scissors

0 score for loss
3 score for tie
6 score for win

1 score for choosing rock
2 score for choosing paper
3 score for choosing scissors
"""

score_table = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3,
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9,
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6,
    },
}


"""
A for Rock
B for Paper
C for Scissors

X means you need to lose
Y means you need to end the round in a draw
Z means you need to win

X for Rock
Y for Paper
Z for Scissors
"""
decision_table = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z",
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    },
}


def part_01():
    score = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_02")) as f:
        for line in f.readlines():
            them, me = line.rstrip().split(" ")
            score += score_table[them][me]
    return score


def part_02():
    score = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_02")) as f:
        for line in f.readlines():
            them, condition = line.rstrip().split(" ")
            me = decision_table[them][condition]
            score += score_table[them][me]
    return score


if __name__ == "__main__":
    print(f"Part 1: Score is {part_01()}.")
    print(f"Part 2: Score is {part_02()}.")
