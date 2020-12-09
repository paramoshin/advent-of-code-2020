"""Advent of code 2020 day 7."""

from typing import List, Set, Tuple

import pytest

from utils import read_input


def find_outer_bags(rules: List[str], color: str) -> Set[str]:
    outer_bags = set()
    colors_q = [color]
    while colors_q:
        color = colors_q.pop()
        for rule in rules:
            outer_bag, inner_bags = rule.split(" bags contain ")
            if color in inner_bags:
                outer_bags.add(outer_bag)
                colors_q.append(outer_bag)
    return outer_bags


def get_inner_bags(rules: List[str], color: str) -> List[Tuple[str, int]]:
    inner_bags = []
    colors_q = [color]
    while colors_q:
        color = colors_q.pop()
        for rule in rules:
            parent, childs = rule.split(" bags contain ")
            if color in parent:
                if childs != "no other bags.":
                    for child in childs.split(", "):
                        count, child_color = child.split(" ", 1)
                        child_color = child_color.rstrip(".").rstrip(" bag").rstrip(" bags")
                        inner_bags.append((child_color, int(count)))
                        for _ in range(int(count)):
                            colors_q.append(child_color)
    return inner_bags


def part1(s: str) -> int:
    rules = s.split("\n")
    bags = find_outer_bags(rules, "shiny gold")
    return len(bags)


def part2(s: str) -> int:
    rules = s.split("\n")
    inner_bags = get_inner_bags(rules, "shiny gold")
    count = 0
    for _, n in inner_bags:
        count += n
    return count


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""",
            4,
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
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""",
            32,
        ),
        (
            """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""",
            126,
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
