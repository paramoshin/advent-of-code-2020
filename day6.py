"""Advent of code 2020 day 6."""

from typing import List

if __name__ == "__main__":
    #     s = """abc

    # a
    # b
    # c

    # ab
    # ac

    # a
    # a
    # a
    # a

    # b"""

    with open("input/day6.txt", "r") as f:
        s = f.read()

    groups = [g.replace("\n", "") for g in s.split("\n\n")]
    count_any = 0
    for group in groups:
        answers = {char for char in group}
        count_any += len(answers)
    print(count_any)

    groups_new: List[List[str]] = [g.split("\n") for g in s.split("\n\n")]
    count_all = 0
    for group_new in groups_new:
        answers = set(group_new[0])
        for i in range(1, len(group_new)):
            answers &= set(group_new[i])
        count_all += len(answers)
    print(count_all)
