import os


def navigate_submarine() -> int:
    depth = 0
    position = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_02")) as f:
        for line in f:
            step, increment = (int(i) if i.isdigit() else i for i in line.strip().split(" "))
            if step in ("up", "down"):
                depth += increment if step == "down" else -increment
            elif step == "forward":
                position += int(increment)
    return depth * position


def navigate_submarine_2() -> int:
    depth = 0
    position = 0
    aim = 0
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_02")) as f:
        for line in f:
            step, increment = (int(i) if i.isdigit() else i for i in line.strip().split(" "))
            if step in ("up", "down"):
                aim += increment if step == "down" else -increment
            elif step == "forward":
                position += increment
                depth += increment * aim
    return depth * position


if __name__ == "__main__":
    print(f"Part 1: {navigate_submarine()}")
    print(f"Part 2: {navigate_submarine_2()}")
