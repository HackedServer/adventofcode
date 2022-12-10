import os


def more_than_one(tail: dict[str, int], head: dict[str, int]) -> bool:
    return any(
        [
            len(
                range(
                    tail["x"] if tail["x"] < head["x"] else head["x"],
                    head["x"] if head["x"] > tail["x"] else tail["x"],
                )
            )
            >= 2,
            len(
                range(
                    tail["y"] if tail["y"] < head["y"] else head["y"],
                    head["y"] if head["y"] > tail["y"] else tail["y"],
                )
            )
            >= 2,
        ]
    )


def part_01() -> int:
    visited: dict[tuple[int, int], bool] = {(0, 0): True}
    t_position = {"x": 0, "y": 0}
    h_position = {"x": 0, "y": 0}
    last_h_position = {"x": 0, "y": 0}

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_09")) as f:
        for line in f.read().splitlines():
            direction, amount = line.split(" ")

            for i in range(int(amount)):
                last_h_position = h_position.copy()
                if direction == "R":
                    h_position["x"] += 1
                elif direction == "L":
                    h_position["x"] -= 1
                elif direction == "U":
                    h_position["y"] += 1
                elif direction == "D":
                    h_position["y"] -= 1
                if more_than_one(t_position, h_position):
                    t_position = last_h_position.copy()
                    visited[(t_position["x"], t_position["y"])] = True

    return len(visited)


def part_02() -> int:
    visited: dict[tuple[int, int], bool] = {(1, 1): True}
    positions = {}
    for i in range(10):
        # Set up the segment starting positions, 0 is head.
        positions[i] = {"x": 1, "y": 1}

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_09")) as f:
        for line in f.read().splitlines():
            direction, amount = line.split(" ")

            for i in range(int(amount)):

                if direction == "R":
                    positions[0]["x"] += 1
                elif direction == "L":
                    positions[0]["x"] -= 1
                elif direction == "U":
                    positions[0]["y"] += 1
                elif direction == "D":
                    positions[0]["y"] -= 1

                for segment in range(1, 10):
                    if more_than_one(positions[segment - 1], positions[segment]):
                        # Ok, its more than 1, now to figure out what move to make

                        # Determine if diagonal is needed
                        if all(
                            [
                                positions[segment - 1]["x"] != positions[segment]["x"],
                                positions[segment - 1]["y"] != positions[segment]["y"],
                            ]
                        ):
                            positions[segment]["x"] += (
                                1 if positions[segment - 1]["x"] - positions[segment]["x"] > 0 else -1
                            )
                            positions[segment]["y"] += (
                                1 if positions[segment - 1]["y"] - positions[segment]["y"] > 0 else -1
                            )

                        # Try moving x
                        elif not more_than_one(
                            positions[segment - 1],
                            {
                                "x": positions[segment]["x"]
                                + (1 if positions[segment - 1]["x"] > positions[segment]["x"] else -1),
                                "y": positions[segment]["y"],
                            },
                        ):
                            positions[segment]["x"] += (
                                1 if positions[segment - 1]["x"] > positions[segment]["x"] else -1
                            )

                        # Try moving y
                        elif not more_than_one(
                            positions[segment - 1],
                            {
                                "x": positions[segment]["x"],
                                "y": positions[segment]["y"]
                                + (1 if positions[segment - 1]["y"] > positions[segment]["y"] else -1),
                            },
                        ):
                            positions[segment]["y"] += (
                                1 if positions[segment - 1]["y"] > positions[segment]["y"] else -1
                            )

                    if segment == 9:
                        visited[(positions[segment]["x"], positions[segment]["y"])] = True

    return len(visited)


if __name__ == "__main__":

    print(f"Part 1: Visted squares = {part_01()}.")
    print(f"Part 2: Visted squares = {part_02()}.")
