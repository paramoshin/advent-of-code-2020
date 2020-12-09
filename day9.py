from typing import List, Tuple


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


if __name__ == "__main__":
    # s = """\
    # 35
    # 20
    # 15
    # 25
    # 47
    # 40
    # 62
    # 55
    # 65
    # 95
    # 102
    # 117
    # 150
    # 182
    # 127
    # 219
    # 299
    # 277
    # 309
    # 576"""

    with open("input/day9.txt", "r") as f:
        s = f.read()

    numbers = [int(n) for n in s.split("\n") if n != ""]
    n = find_wrong_number(numbers, 25)
    print(n)

    min_n, max_n = find_contigious_set(numbers, n)
    print(min_n, max_n)
    print(min_n + max_n)
