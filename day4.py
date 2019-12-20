#!/usr/bin/env python
import pytest

PUZZLE_INPUT = "273025-767253"


def increasing(number, submatching=False):
    num = number
    last = 0
    repeated_chars = {}
    for dec in [100_000, 10_000, 1_000, 100, 10, 1]:
        a = num // dec
        repeated_chars[a] = 1 if a not in repeated_chars else repeated_chars[a] + 1
        num -= a * dec
        if a < last:
            return False
        elif a == last:
            last = a
        else:
            last = a
    if submatching:
        return 2 in repeated_chars.values()
    else:
        return any(x in repeated_chars.values() for x in [2, 3, 4, 5])


def increasing_part1(number):
    return increasing(number, submatching=False)


def increasing_part2(number):
    return increasing(number, submatching=True)


def solve1(start, end):
    return len(set(filter(increasing_part1, range(start, end + 1))))


def solve2(start, end):
    return len(set(filter(increasing_part2, range(start, end + 1))))


@pytest.mark.parametrize(
    "number, result", [(123455, True), (122345, True), (412345, False), (123444, True)]
)
def test_increasing1(number, result):
    assert result == increasing_part1(number)


@pytest.mark.parametrize(
    "number, result",
    [(123455, True), (122345, True), (412345, False), (111122, True), (123444, False)],
)
def test_increasing2(number, result):
    assert result == increasing_part2(number)


def main():
    start, end = map(int, PUZZLE_INPUT.split("-"))
    print("Part1=" + str(solve1(start, end)))
    print("Part2=" + str(solve2(start, end)))


if __name__ == "__main__":
    main()
