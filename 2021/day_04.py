import os
from typing import List, Optional

DRAWN_NUMBERS: List[int] = []


class BingoBoard:
    board: List[List[int]]
    board_rotated: List[List[int]]

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.board_rotated = [list(row) for row in zip(*self.board)]

    @classmethod
    def from_input(cls, data: List[str]) -> "BingoBoard":
        board = list()
        for line in data[1:6]:
            board.append([int(i) for i in line.strip().split()])
        return cls(board)

    def unmatched_numbers(self, all_draws: List[int]) -> List[int]:
        unmatch: List[int] = []
        for i in [j for l in self.board for j in l]:
            if i not in all_draws:
                unmatch.append(i)
        return unmatch

    def check_hits(self, numbers: List[int]) -> bool:
        for row in self.board_rotated + self.board:
            if len(set(row) & set(numbers)) == 5:
                return True
        return False


def build_state() -> List[BingoBoard]:
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_04")) as f:
        global DRAWN_NUMBERS
        DRAWN_NUMBERS = [int(i) for i in f.readline().strip().split(",")]
        input = f.readlines()
    return [BingoBoard.from_input(input[i : i + 6]) for i in range(0, len(input), 6)]


def part_01() -> int:
    boards = build_state()
    current_draws: List[int] = []
    winner: Optional[BingoBoard] = None
    for draw in DRAWN_NUMBERS:
        current_draws.append(draw)
        if len(current_draws) < 5:
            continue
        for board in boards:
            if board.check_hits(current_draws):
                winner = board
                break
        if winner:
            break

    return sum(winner.unmatched_numbers(current_draws)) * current_draws[-1]


def part_02() -> int:
    boards = build_state()
    current_draws: List[int] = []
    last_winner: Optional[BingoBoard] = None
    last_winner_draws: Optional[List[int]] = None
    for draw in DRAWN_NUMBERS:
        current_draws.append(draw)
        if len(current_draws) < 5:
            continue
        for board in boards.copy():
            if board.check_hits(current_draws):
                last_winner = board
                last_winner_draws = current_draws.copy()
                boards.remove(board)

    return sum(last_winner.unmatched_numbers(last_winner_draws)) * last_winner_draws[-1]


if __name__ == "__main__":
    print(f"Part 01: {part_01()}")
    print(f"Part 02: {part_02()}")
