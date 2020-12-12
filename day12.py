"""Advent of code 2020 day 0."""

from dataclasses import dataclass
from typing import Literal, NamedTuple, Tuple

import pytest

from utils import read_input

Directions = Literal["N", "S", "E", "W"]


@dataclass
class Ferry:
    _directions: Tuple[Directions, ...] = ("N", "E", "S", "W")
    direction: Directions = "E"
    x: int = 0
    y: int = 0
    waypoint = {"x": 10, "y": 1}

    @staticmethod
    def _parse_command(command: str) -> Tuple[str, int]:
        action, value = command[0], int(command[1:])
        return action, value

    def _move_in_direction(self, direction: str, value: int) -> None:
        if direction == "N":
            self.y += value
        elif direction == "S":
            self.y -= value
        elif direction == "E":
            self.x += value
        elif direction == "W":
            self.x -= value

    def execute_command(self, command: str) -> None:
        action, value = self._parse_command(command)
        if action == "R":
            i = value // 90
            ind = self._directions.index(self.direction) + i
            ind = ind - len(self._directions) if ind >= len(self._directions) else ind
            self.direction = self._directions[ind]
        elif action == "L":
            i = value // 90
            ind = self._directions.index(self.direction) - i
            ind = ind - len(self._directions) if ind >= len(self._directions) else ind
            self.direction = self._directions[ind]
        elif action in self._directions:
            self._move_in_direction(action, value)
        elif action == "F":
            self._move_in_direction(self.direction, value)

    def calculate_distance(self):
        return abs(self.x) + abs(self.y)

    def _move_waypoint_in_direction(self, direction: str, value: int) -> None:
        if direction == "N":
            self.waypoint["y"] += value
        elif direction == "S":
            self.waypoint["y"] -= value
        elif direction == "E":
            self.waypoint["x"] += value
        elif direction == "W":
            self.waypoint["x"] -= value

    def _move_waypoint(self, action: str, value: int) -> None:
        if action in self._directions:
            self._move_waypoint_in_direction(action, value)
        elif action == "R":
            i = value // 90
            i = i % 4 if i > 4 else i
            if i == 1:
                self.waypoint["x"], self.waypoint["y"] = self.waypoint["y"], -self.waypoint["x"]
            elif i == 2:
                self.waypoint["x"], self.waypoint["y"] = -self.waypoint["x"], -self.waypoint["y"]
            elif i == 3:
                self.waypoint["x"], self.waypoint["y"] = -self.waypoint["y"], self.waypoint["x"]
        elif action == "L":
            i = value // 90
            i = i % 4 if i > 4 else i
            if i == 1:
                self.waypoint["x"], self.waypoint["y"] = -self.waypoint["y"], self.waypoint["x"]
            elif i == 2:
                self.waypoint["x"], self.waypoint["y"] = -self.waypoint["x"], -self.waypoint["y"]
            elif i == 3:
                self.waypoint["x"], self.waypoint["y"] = self.waypoint["y"], -self.waypoint["x"]

    def _move_ship_to_waypoint(self, action: str, value: int) -> None:
        if action == "F":
            self.x += value * self.waypoint["x"]
            self.y += value * self.waypoint["y"]

    def execute_new_command(self, command: str) -> None:
        action, value = self._parse_command(command)
        self._move_waypoint(action, value)
        self._move_ship_to_waypoint(action, value)


def part1(s: str) -> int:
    commands = s.splitlines()
    ferry = Ferry()
    for command in commands:
        ferry.execute_command(command)
    distance = ferry.calculate_distance()
    return distance


def part2(s: str) -> int:
    commands = s.splitlines()
    ferry = Ferry()
    for command in commands:
        ferry.execute_new_command(command)
    distance = ferry.calculate_distance()
    return distance


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
F10
N3
F7
R90
F11""",
            25,
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
F10
N3
F7
R90
F11""",
            286,
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
