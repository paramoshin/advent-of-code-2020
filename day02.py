"""Advent of code 2020 day 2."""

from typing import Tuple

import pytest

from utils import read_input


def parse_policy(policy_str: str) -> Tuple[str, int, int]:
    letter, min_occ, max_occ = (
        policy_str.split(" ")[1],
        int(policy_str.split(" ")[0].split("-")[0]),
        int(policy_str.split(" ")[0].split("-")[1]),
    )
    return letter, min_occ, max_occ


def is_valid(line: str) -> bool:
    policy_str, password = line.split(": ")[0], line.split(": ")[1]
    letter, min_occ, max_occ = parse_policy(policy_str)
    n_occ = 0
    for char in password:
        if char == letter:
            n_occ += 1
    return min_occ <= n_occ <= max_occ


def is_valid_new(line: str) -> bool:
    policy_str, password = line.split(": ")[0], line.split(": ")[1]
    letter, min_occ, max_occ = parse_policy(policy_str)
    return (password[min_occ - 1] == letter and password[max_occ - 1] != letter) or (
        password[min_occ - 1] != letter and password[max_occ - 1] == letter
    )


def part1(s: str) -> int:
    n_valid = 0
    for line in s.split("\n"):
        n_valid += is_valid(line)
    return n_valid


def part2(s: str) -> int:
    n_valid_new = 0
    for line in s.split("\n"):
        n_valid_new += is_valid_new(line)
    return n_valid_new


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""",
            2,
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
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""",
            1,
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
