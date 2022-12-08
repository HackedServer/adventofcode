import os


def parse_input() -> list[list[int]]:
    regular = []

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_08")) as f:
        for line in f.read().splitlines():
            regular.append([*line])

    return regular


def check_if_visible(input, row, column) -> bool:
    tree_height = input[row][column]
    # Check left
    if all([height < tree_height for height in input[row][:column]]):
        return True

    # Check right
    if all([height < tree_height for height in input[row][column + 1 :]]):
        return True

    # Check down
    if all(
        [
            height < tree_height
            for height in [input[x][column] for x in range(row + 1, len(input))]
        ]
    ):
        return True

    # Check up
    if all(
        [height < tree_height for height in [input[x][column] for x in range(0, row)]]
    ):
        return True


def part_01(regular) -> int:
    visible = 0

    for e in range(len(regular)):
        for i in range(len(regular[0])):
            if check_if_visible(regular, e, i):
                visible += 1

    return visible


def get_scenic_score(input, row, column) -> int:
    tree_height = input[row][column]
    left = [height for height in input[row][:column]]
    left = list(reversed(left))
    right = [height for height in input[row][column + 1 :]]
    down = [height for height in [input[x][column] for x in range(row + 1, len(input))]]
    up = [height for height in [input[x][column] for x in range(0, row)]]
    up = list(reversed(up))

    # Left score
    left_score = 0
    for height in left:
        if height >= tree_height:
            left_score += 1
            break
        left_score += 1

    # Right score
    right_score = 0
    for height in right:
        if height >= tree_height:
            right_score += 1
            break
        right_score += 1

    # Down score
    down_score = 0
    for height in down:
        if height >= tree_height:
            down_score += 1
            break
        down_score += 1

    # Up score
    up_score = 0
    for height in up:
        if height >= tree_height:
            up_score += 1
            break
        up_score += 1
    return right_score * left_score * down_score * up_score


def part_02(regular):
    best = 0
    for e in range(len(regular)):
        for i in range(len(regular[0])):
            score = get_scenic_score(regular, e, i)
            if score > best:
                best = score

    return best


if __name__ == "__main__":
    regular = parse_input()
    print(f"Part 1: Number is visble trees: {part_01(regular)}.")
    print(f"Part 2: The best scenic score is {part_02(regular)}.")
