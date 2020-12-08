from typing import List


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
#     s = """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#"""
#     lines = [line for line in s.split("\n")]

    with open("input/day3.txt", "r") as f:
        lines = f.read().splitlines()
    
    print(check_slope(lines, 1, 3))

    steps = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    count = 1
    for down, right in steps:
        count *= check_slope(lines, down, right)
    print(count)
