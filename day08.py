"""Advent of code 2020 day 8."""

from typing import List, Tuple

import pytest

from utils import read_input


def run_code(commands: List[str]) -> Tuple[str, int]:
    call_count = {}
    acc = 0
    i = 0
    status = ""
    while True:
        if i in call_count:
            status = "error"
            break
        elif i >= len(commands):
            status = "ok"
            break
        else:
            call_count[i] = 1
        command = commands[i]

        operation, args = command.split(" ")
        sign = args[0]
        value = int(args[1:])

        if operation == "nop":
            i += 1
        elif operation == "acc":
            if sign == "-":
                acc -= value
            elif sign == "+":
                acc += value
            i += 1
        elif operation == "jmp":
            if sign == "-":
                i -= value
            elif sign == "+":
                i += value
    return status, acc


def fix_program(commands: List[str]) -> Tuple[str, int]:
    for i, command in enumerate(commands):
        if "nop" in command:
            original_command = command
            commands[i] = command.replace("nop", "jmp")
            status, acc = run_code(commands)
            if status == "ok":
                return status, acc
            else:
                commands[i] = original_command
        if "jmp" in command:
            original_command = command
            commands[i] = command.replace("jmp", "nop")
            status, acc = run_code(commands)
            if status == "ok":
                return status, acc
            else:
                commands[i] = original_command
    return "error", 0


def part1(s: str) -> int:
    commands = s.split("\n")
    _, acc = run_code(commands)
    return acc


def part2(s: str) -> int:
    commands = s.split("\n")
    _, acc = fix_program(commands)
    return acc


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""",
            5,
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
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""",
            8,
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
