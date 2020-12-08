from typing import List


def find_product_of_two(nums: List[int], value: int) -> int:
    needs = {value - n for n in nums}
    for n in nums:
        if n in needs:
            return n * (2020 - n)


def find_product_of_three(nums: List[int], value: int) -> int:
    needs = {value - i - j: (i, j) for i in nums for j in nums if i != j}
    for n in nums:
        if n in needs:
            return n * needs[n][0] * needs[n][1]


if __name__ == "__main__":
    nums = []
    with open("input/day1.txt", "r") as f:
        lines = f.readlines()

    nums = [int(x.strip()) for x in lines]

    print(find_product_of_two(nums, 2020))
    print(find_product_of_three(nums, 2020))
