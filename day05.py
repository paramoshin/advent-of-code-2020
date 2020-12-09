"""Advent of code 2020 day 5."""

from math import ceil
from typing import Tuple

import pytest

from utils import read_input


def find(s: str, upper_limit: int, upper_char: str, lower_char: str) -> int:
    l, u = 0, upper_limit
    for char in s:
        if char == lower_char:
            u = l + int((u - l) / 2)
        elif char == upper_char:
            l = l + ceil((u - l) / 2)
    return l


def part1(s: str) -> int:
    lines = s.split("\n")
    seat_ids = []
    for s in lines:
        row = find(s, 127, "B", "F")
        col = find(s, 7, "R", "L")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
    return max(seat_ids)


def part2(s: str) -> int:
    lines = s.split("\n")
    seat_ids = []
    for s in lines:
        row = find(s, 127, "B", "F")
        col = find(s, 7, "R", "L")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
    seat_ids.sort()
    for i in range(1, len(seat_ids)):
        if seat_ids[i - 1] + 2 == seat_ids[i]:
            return seat_ids[i - 1] + 1
    return 0


@pytest.mark.parametrize(
    "test_input, expected",
    (("FBFBBFFRLR", 357),),
)
def test_part1(test_input: str, expected: int) -> None:
    assert part1(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    (("", 0),),
)
def test_part2(test_input: str, expected: int) -> None:
    assert part2(test_input) == expected


def main() -> Tuple[int, int]:
    s = read_input(__file__)
    result_1 = part1(s)
    result_2 = part2(s)
    return result_1, result_2


if __name__ == "__main__":
    result_1, result_2 = main()
    print(result_1, result_2)
