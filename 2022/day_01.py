import os


def part_01() -> int:
    elf_counter: int = 1
    calorie_dict = dict()

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_01")) as f:
        for line in f.readlines():
            if line == "\n":
                elf_counter += 1
            else:
                if calorie_dict.get(elf_counter):
                    calorie_dict[elf_counter] += int(line)
                else:
                    calorie_dict[elf_counter] = int(line)

    return sorted(calorie_dict.items(), key=lambda item: item[1], reverse=True)[0][1]


def part_02() -> int:
    elf_counter: int = 1
    calorie_dict = dict()

    with open(os.path.join(os.path.dirname(__file__), "inputs/day_01")) as f:
        for line in f.readlines():
            if line == "\n":
                elf_counter += 1
            else:
                if calorie_dict.get(elf_counter):
                    calorie_dict[elf_counter] += int(line)
                else:
                    calorie_dict[elf_counter] = int(line)

    sorted_calorie_dict = sorted(
        calorie_dict.items(), key=lambda item: item[1], reverse=True
    )
    return (
        sorted_calorie_dict[0][1]
        + sorted_calorie_dict[1][1]
        + sorted_calorie_dict[2][1]
    )


if __name__ == "__main__":
    print(f"Part 1: Elf with the most calories has {part_01()} calories.")
    print(f"Part 2: The top 3 elves are carrying {part_02()} calories.")
