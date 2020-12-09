"""Advent of code 2020 day 4."""

from typing import Dict, Tuple, Union

import pytest

from utils import read_input


def is_valid(passport: Union[dict, set]) -> bool:
    neccessary_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }
    return all(field in passport for field in neccessary_fields)


def is_valid_strict(passport: dict) -> bool:
    is_valid = False
    try:
        is_valid = (
            1920 <= int(passport.get("byr")) <= 2002  # type: ignore
            and 2010 <= int(passport.get("iyr")) <= 2020  # type: ignore
            and 2020 <= int(passport.get("eyr")) <= 2030  # type: ignore
            and (
                (
                    len(passport.get("hgt")) == 5  # type: ignore
                    and passport.get("hgt")[-2:] == "cm"  # type: ignore
                    and 150 <= int(passport.get("hgt").replace("cm", "")) <= 193  # type: ignore
                )
                or (
                    len(passport.get("hgt")) == 4  # type: ignore
                    and passport.get("hgt")[-2:] == "in"  # type: ignore
                    and 59 <= int(passport.get("hgt").replace("in", "")) <= 76  # type: ignore
                )
            )
            and (len(passport.get("hcl")) == 7 and passport.get("hcl")[0] == "#" and passport.get("hcl")[1:].isalnum())  # type: ignore
            and passport.get("ecl") in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}  # type: ignore
            and (len(passport.get("pid")) == 9 and passport.get("pid").isnumeric())  # type: ignore
        )
    except Exception as e:
        return False
    return is_valid


def part1(s: str) -> int:
    passports = [{x.split(":")[0]: x.split(":")[1] for x in p.replace("\n", " ").split(" ")} for p in s.split("\n\n")]
    count_valid = 0
    for passport in passports:
        count_valid += is_valid(passport)
    return count_valid


def part2(s: str) -> int:
    passports = [{x.split(":")[0]: x.split(":")[1] for x in p.replace("\n", " ").split(" ")} for p in s.split("\n\n")]
    count_strict_valid = 0
    for passport in passports:
        count_strict_valid += is_valid_strict(passport)
    return count_strict_valid


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""",
            2,
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
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""",
            0,
        ),
        (
            """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""",
            4,
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
