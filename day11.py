"""Advent of code 2020 day 0."""

from typing import Dict, List, Tuple

import pytest

from utils import read_input


def parse_seats(seats: List[List[str]]) -> Dict[Tuple[int, int], str]:
    seats_dict = {}
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            seats_dict[(i, j)] = seats[i][j]
    return seats_dict


def get_adjacent(i: int, j: int, n_rows: int, n_cols: int) -> List[Tuple[int, int]]:
    adj = []
    for i_ in (-1, 0, 1):
        for j_ in (-1, 0, 1):
            if i_ == 0 and j_ == 0:
                continue
            if i >= -i_ and i < n_rows - i_ and j >= -j_ and j < n_cols - j_:
                adj.append((i + i_, j + j_))
    return adj


def get_visible(seats: Dict[Tuple[int, int], str], i: int, j: int, n_rows: int, n_cols: int) -> List[Tuple[int, int]]:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    visible = []
    for x, y in directions:
        x_, y_ = i + x, j + y
        while x_ < n_rows and y_ < n_cols and x_ >= 0 and y_ >= 0:
            value = seats[(x_, y_)]
            if value != ".":
                visible.append((x_, y_))
                break
            x_ += x
            y_ += y
    return visible


def part1(s: str) -> int:
    seats_ = [list(line) for line in s.split("\n") if line != ""]
    n_rows = len(seats_)
    n_cols = len(seats_[0])
    seats = parse_seats(seats_)
    while True:
        rounds = 0
        changes = {}
        for (i, j), v in seats.items():
            if v == ".":
                continue
            adjacent = get_adjacent(i, j, n_rows, n_cols)
            if seats[(i, j)] == "L":
                adj_count = 0
                for x, y in adjacent:
                    if seats[(x, y)] == "#":
                        adj_count += 1
                if adj_count == 0:
                    changes[(i, j)] = "#"
            elif seats[(i, j)] == "#":
                adj_count = 0
                for x, y in adjacent:
                    if seats[(x, y)] == "#":
                        adj_count += 1
                if adj_count >= 4:
                    changes[(i, j)] = "L"
        if not changes:
            break
        for (i, j), v in changes.items():
            seats[(i, j)] = v
    count_occupied = 0
    for _, v in seats.items():
        if v == "#":
            count_occupied += 1
    return count_occupied


def part2(s: str) -> int:
    seats_ = [list(line) for line in s.split("\n") if line != ""]
    n_rows = len(seats_)
    n_cols = len(seats_[0])
    seats = parse_seats(seats_)
    while True:
        changes = {}
        for (i, j), v in seats.items():
            if v == ".":
                continue
            visible = get_visible(seats, i, j, n_rows, n_cols)
            if seats[(i, j)] == "L":
                vis_occupied = 0
                for x, y in visible:
                    if seats[(x, y)] == "#":
                        vis_occupied += 1
                if vis_occupied == 0:
                    changes[(i, j)] = "#"
            elif seats[(i, j)] == "#":
                vis_occupied = 0
                for x, y in visible:
                    if seats[(x, y)] == "#":
                        vis_occupied += 1
                if vis_occupied >= 5:
                    changes[(i, j)] = "L"
        if not changes:
            break
        for (i, j), v in changes.items():
            seats[(i, j)] = v
    count_occupied = 0
    for _, v in seats.items():
        if v == "#":
            count_occupied += 1
    return count_occupied


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""",
            37,
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
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""",
            26,
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
