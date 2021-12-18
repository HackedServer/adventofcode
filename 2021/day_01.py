import os
from typing import Optional, List


def count_depth_increase() -> int:
    """
    Reads inputs/day_01 and returns the number of times the number inceases.
    """
    total_increases: int = 0
    last_value: Optional[int] = None
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_01")) as f:
        for line in f.readlines():
            cur = int(line)
            if last_value is not None and cur > last_value:
                total_increases += 1
            last_value = cur
    return total_increases


def count_depth_increase_window() -> int:
    """
    Reads inputs/day_01 and returns the number of times a sliding 3 measurement window increases
    """
    total_increases: int = 0
    prev_sum: Optional[int] = None

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_01")) as f:
        values = [int(line) for line in f.readlines()]
        for i in range(len(values) - 2):
            cur_sum = sum(values[i : i + 3])
            if prev_sum is not None and cur_sum > prev_sum:
                total_increases += 1
            prev_sum = cur_sum
    return total_increases


if __name__ == "__main__":
    print(f"Part 1: {count_depth_increase()} increases")
    print(f"Part 2: {count_depth_increase_window()} increases")
