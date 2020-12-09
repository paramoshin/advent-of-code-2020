"""Advent of code 2020 day 0."""

from typing import Tuple

import pytest

from utils import read_input


def part1(s: str) -> int:
    return 0


def part2(s: str) -> int:
    return 0


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
            """,
            0,
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
            """,
            0,
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
