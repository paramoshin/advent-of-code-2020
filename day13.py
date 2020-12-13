"""Advent of code 2020 day 0."""

from typing import Tuple

import pytest
from sympy.ntheory.modular import crt

from utils import read_input


def part1(s: str) -> int:
    timestamp_str, buses_str = s.splitlines()[0], s.splitlines()[1]
    timestamp = int(timestamp_str)
    buses = [int(x) for x in buses_str.split(",") if x != "x"]
    can_depart_at = timestamp
    while True:
        for bus in buses:
            if can_depart_at % bus == 0:
                return bus * (can_depart_at - timestamp)
        can_depart_at += 1


def part2(s: str) -> int:
    line = s.splitlines()[1]
    buses = [(i, int(x)) for i, x in enumerate(line.split(",")) if x != "x"]
    bus_ids = [bus[1] for bus in buses]
    mods = [-1 * bus[0] for bus in buses]

    return crt(bus_ids, mods)[0]


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
939
7,13,x,x,59,x,31,19""",
            295,
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
939
7,13,x,x,59,x,31,19""",
            1068781,
        ),
        (
            """\
939
17,x,13,19""",
            3417,
        ),
        (
            """\
939
67,7,59,61""",
            754018,
        ),
        (
            """\
939
67,x,7,59,61""",
            779210,
        ),
        (
            """\
939
67,7,x,59,61""",
            1261476,
        ),
        (
            """\
939
1789,37,47,1889""",
            1202161486,
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
