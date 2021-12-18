import os
from typing import List, Dict, Optional


def get_input() -> List[str]:
    with open(os.path.join(os.path.dirname(__file__), "inputs/day_03")) as f:
        return f.read().splitlines()


def get_most_common_characters(data: Optional[List[str]] = get_input()) -> List[str]:
    bits: Dict[str, List[int]] = dict()

    for line in data:
        for idx, val in enumerate(list(line.strip())):
            bits.setdefault(idx, []).append(val)
    most_common: List[str] = list()
    for position in bits.keys():
        if bits[position].count("1") >= bits[position].count("0"):
            most_common.append("1")
        else:
            most_common.append("0")
    return most_common


def get_most_common_character(data: List[str], postion: int) -> str:
    return get_most_common_characters(data)[postion]


def get_power_consumption() -> int:
    most_common = get_most_common_characters()
    gamma_rate = "".join(most_common)
    epsilon_rate = "".join(["1" if i == "0" else "0" for i in most_common])

    return int(epsilon_rate, 2) * int(gamma_rate, 2)


def get_power_consumption_2() -> int:
    source = get_input()
    oxygen_list = source.copy()
    for i in range(0, len(source[0])):
        match_char = get_most_common_character(oxygen_list, i)
        for line in oxygen_list.copy():
            if list(line)[i] != match_char:
                oxygen_list.remove(line)
        if len(oxygen_list) == 1:
            break

    print(oxygen_list)

    co2_list = source.copy()
    for i in range(0, len(source[0])):
        match_char = "0" if get_most_common_character(co2_list, i) == "1" else "1"
        for line in co2_list.copy():
            if list(line)[i] != match_char:
                co2_list.remove(line)
        if len(co2_list) == 1:
            break

    print(co2_list)
    return int(co2_list[0], 2) * int(oxygen_list[0], 2)


if __name__ == "__main__":
    print(f"Part 1: {get_power_consumption()}")
    print(f"Part 2: {get_power_consumption_2()}")
