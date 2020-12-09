"""Some often used functions."""

from pathlib import Path
from typing import List


def read_input(file: str) -> str:
    input_path = f"input/{Path(file).stem}.txt"
    with open(input_path, "r") as f:
        s = f.read()
    return s


def input_to_int(s: str) -> List[int]:
    return [int(n.strip()) for n in s.split("\n") if n != ""]
