"""Advent of code 2020 day 6."""

from typing import List, Tuple

import pytest

from utils import read_input


def part1(s: str) -> int:
    groups = [g.replace("\n", "") for g in s.split("\n\n")]
    count_any = 0
    for group in groups:
        answers = {char for char in group}
        count_any += len(answers)
    return count_any


def part2(s: str) -> int:
    groups: List[List[str]] = [g.split("\n") for g in s.split("\n\n")]
    count_all = 0
    for group in groups:
        answers = set(group[0])
        for i in range(1, len(group)):
            answers &= set(group[i])
        count_all += len(answers)
    return count_all


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
abc

a
b
c

ab
ac

a
a
a
a

b""",
            11,
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
abc

a
b
c

ab
ac

a
a
a
a

b""",
            6,
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
