"""Advent of code 2020 day 7."""

from typing import List, Set, Tuple


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


if __name__ == "__main__":
    #     rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    # dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    # bright white bags contain 1 shiny gold bag.
    # muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    # shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    # dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    # vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    # faded blue bags contain no other bags.
    # dotted black bags contain no other bags.""".split("\n")

    #     rules = """shiny gold bags contain 2 dark red bags.
    # dark red bags contain 2 dark orange bags.
    # dark orange bags contain 2 dark yellow bags.
    # dark yellow bags contain 2 dark green bags.
    # dark green bags contain 2 dark blue bags.
    # dark blue bags contain 2 dark violet bags.
    # dark violet bags contain no other bags.""".split("\n")

    with open("input/day7.txt", "r") as f:
        rules = f.read().splitlines()

    bags = find_outer_bags(rules, "shiny gold")
    print(len(bags))

    inner_bags = get_inner_bags(rules, "shiny gold")
    count = 0
    for _, n in inner_bags:
        count += n
    print(count)
