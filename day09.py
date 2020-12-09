"""Advent of code 2020 day9."""

from typing import List, Tuple

import pytest

from utils import input_to_int, read_input


def find_wrong_number(numbers: List[int], preamble_len: int) -> int:
    for i in range(preamble_len, len(numbers)):
        is_valid = 0
        previous = set(numbers[i - preamble_len : i])
        for n in previous:
            if is_valid == 1:
                continue
            residue = numbers[i] - n
            if residue in previous:
                is_valid = 1
        if is_valid == 0:
            return numbers[i]
    return 0


def find_contigious_set(numbers: List[int], n: int) -> Tuple[int, int]:
    for i, current_number in enumerate(numbers):
        s = current_number
        ns = [current_number]
        for j in range(i + 1, len(numbers)):
            s += numbers[j]
            ns.append(numbers[j])
            if s == n:
                return min(ns), max(ns)
            elif s > n:
                break
    return 0, 0


def part1(s: str, preamble_len: int) -> int:
    numbers = input_to_int(s)
    n = find_wrong_number(numbers, preamble_len)
    return n


def part2(s: str, n: int) -> int:
    numbers = input_to_int(s)
    min_n, max_n = find_contigious_set(numbers, n)
    return min_n + max_n


@pytest.mark.parametrize(
    "test_input, preamble_len, expected",
    (
        (
            """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""",
            5,
            127,
        ),
    ),
)
def test_part1(test_input: str, preamble_len: int, expected: int) -> None:
    assert part1(test_input, preamble_len) == expected


@pytest.mark.parametrize(
    "test_input, n, expected",
    (
        (
            """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""",
            127,
            62,
        ),
    ),
)
def test_pat2(test_input: str, n: int, expected: int) -> None:
    assert part2(test_input, n) == expected


def main() -> Tuple[int, int]:
    s = read_input(__file__)
    result_1 = part1(s, 25)
    result_2 = part2(s, result_1)
    return result_1, result_2


if __name__ == "__main__":
    result_1, result_2 = main()
    print(result_1, result_2)
