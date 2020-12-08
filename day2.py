from typing import Tuple


def parse_policy(policy_str: str) -> Tuple[str, int, int]:
    letter, min_occ, max_occ = (
        policy_str.split(" ")[1], 
        int(policy_str.split(" ")[0].split("-")[0]), 
        int(policy_str.split(" ")[0].split("-")[1])
    )
    return letter, min_occ, max_occ


def is_valid(line: str) -> bool:
    policy_str, password = line.split(": ")[0], line.split(": ")[1]
    letter, min_occ, max_occ = parse_policy(policy_str)
    n_occ = 0
    for char in password:
        if char == letter:
            n_occ += 1
    return min_occ <= n_occ <= max_occ


def is_valid_new(line: str) -> bool:
    policy_str, password = line.split(": ")[0], line.split(": ")[1]
    letter, min_occ, max_occ = parse_policy(policy_str)
    return (
        (password[min_occ - 1] == letter and password[max_occ - 1] != letter) 
        or 
        (password[min_occ - 1] != letter and password[max_occ - 1] == letter)
    )


if __name__ == "__main__":
    with open("input/day2.txt", "r") as f:
        lines = f.readlines()

    n_valid = 0
    n_valid_new = 0
    for line in lines:
        n_valid += is_valid(line)
        n_valid_new += is_valid_new(line)
    print(n_valid)
    print(n_valid_new)

