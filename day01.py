"""Advent of code 2020 day 1."""

from typing import List, Tuple

import pytest

from utils import input_to_int, read_input


def find_product_of_two(nums: List[int], value: int) -> int:
    needs = {value - n for n in nums}
    for n in nums:
        if n in needs:
            return n * (2020 - n)
    return 0


def find_product_of_three(nums: List[int], value: int) -> int:
    needs = {value - i - j: (i, j) for i in nums for j in nums if i != j}
    for n in nums:
        if n in needs:
            return n * needs[n][0] * needs[n][1]
    return 0


def part1(s: str) -> int:
    nums = input_to_int(s)
    return find_product_of_two(nums, 2020)


def part2(s: str) -> int:
    nums = input_to_int(s)
    return find_product_of_three(nums, 2020)


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
1721
979
366
299
675
1456""",
            514579,
        ),
    ),
)
def test_part1(test_input: str, expected: int) -> None:
    assert part1(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
1721
979
366
299
675
1456""",
            241861950,
        ),
    ),
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
