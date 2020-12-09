"""Advent of code 2020 day 5."""

from math import ceil
from typing import Tuple


def find(s: str, upper_limit: int, upper_char: str, lower_char: str) -> int:
    l, u = 0, upper_limit
    for char in s:
        if char == lower_char:
            u = l + int((u - l) / 2)
        elif char == upper_char:
            l = l + ceil((u - l) / 2)
    return l


if __name__ == "__main__":
    # lines = [
    #     "FBFBBFFRLR",
    #     "BFFFBBFRRR",
    #     "FFFBBBFRRR",
    #     "BBFFBBFRLL",
    # ]

    with open("input/day5.txt", "r") as f:
        lines = f.read().splitlines()

    seat_ids = []
    for s in lines:
        row = find(s, 127, "B", "F")
        col = find(s, 7, "R", "L")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
        # print(row, col, seat_id)
    print(max(seat_ids))

    seat_ids.sort()
    for i in range(1, len(seat_ids)):
        if seat_ids[i - 1] + 2 == seat_ids[i]:
            print(seat_ids[i - 1] + 1)
            break
