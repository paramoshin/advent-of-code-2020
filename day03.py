"""Advent of code 2020 day 3."""

from typing import List, Tuple

import pytest

from utils import read_input


def part1(s: str) -> int:
    lines = s.split("\n")
    res = check_slope(lines, 1, 3)
    return res


def part2(s: str) -> int:
    lines = s.split("\n")
    steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    count = 1
    for down, right in steps:
        count *= check_slope(lines, down, right)
    return count


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""",
            7,
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
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""",
            336,
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


def check_slope(lines: List[str], down: int, right: int) -> int:
    i = 0
    j = 0
    trees_count = 0
    while True:
        j += right
        if j >= len(lines[i]):
            j = j - len(lines[i])
        i += down
        if i >= len(lines):
            break
        if lines[i][j] == "#":
            trees_count += 1
    return trees_count


if __name__ == "__main__":
    result_1, result_2 = main()
    print(result_1, result_2)
