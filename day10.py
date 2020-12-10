"""Advent of code 2020 day 10."""

from typing import Tuple

import pytest

from utils import input_to_int, read_input


def part1(s: str) -> int:
    adapters = input_to_int(s)
    adapters.append(0)
    adapters.sort()
    jolt_1 = 0
    jolt_3 = 1
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] > 3:
            break
        elif adapters[i + 1] - adapters[i] == 1:
            jolt_1 += 1
        elif adapters[i + 1] - adapters[i] > 1:
            jolt_3 += 1
    return jolt_1 * jolt_3


def part2(s: str) -> int:
    adapters = input_to_int(s)
    adapters.append(0)
    adapters.sort()
    dp = [0] * len(adapters)
    dp[0] = 1
    for i in range(len(adapters)):
        for j in range(1, 4):
            if j > i:
                break
            elif adapters[i] <= adapters[i - j] + 3:
                dp[i] += dp[i - j]
    return dp[-1]


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
16
10
15
5
1
11
7
19
6
12
4""",
            7 * 5,
        ),
        (
            """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""",
            22 * 10,
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
16
10
15
5
1
11
7
19
6
12
4""",
            8,
        ),
        (
            """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""",
            19208,
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
