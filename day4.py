#!/usr/bin/env python
import pytest
import concurrent.futures
import itertools


PUZZLE_INPUT = "273025-767253"


def increasing(number):
    num = number
    last = 0
    equal_found = False
    for dec in [100_000, 10_000, 1_000, 100, 10, 1]:
        a = num // dec
        num -= a * dec
        if a < last:
            return False
        elif a == last:
            equal_found = True
            last = a
        else:
            last = a
    return True and equal_found


def solve(start, end):
    return len(set(filter(increasing, range(start, end + 1))))


@pytest.mark.parametrize(
    "number, result", [(123455, True), (122345, True), (412345, False)]
)
def test_increasing(number, result):
    assert result == increasing(number)


def main():
    start, end = map(int, PUZZLE_INPUT.split("-"))
    print(solve(start, end))


if __name__ == "__main__":
    main()

