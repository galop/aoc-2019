#!/usr/bin/env python
import copy
import pytest
import math

TEST_DATA = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    13,
    1,
    19,
    1,
    6,
    19,
    23,
    2,
    6,
    23,
    27,
    1,
    5,
    27,
    31,
    2,
    31,
    9,
    35,
    1,
    35,
    5,
    39,
    1,
    39,
    5,
    43,
    1,
    43,
    10,
    47,
    2,
    6,
    47,
    51,
    1,
    51,
    5,
    55,
    2,
    55,
    6,
    59,
    1,
    5,
    59,
    63,
    2,
    63,
    6,
    67,
    1,
    5,
    67,
    71,
    1,
    71,
    6,
    75,
    2,
    75,
    10,
    79,
    1,
    79,
    5,
    83,
    2,
    83,
    6,
    87,
    1,
    87,
    5,
    91,
    2,
    9,
    91,
    95,
    1,
    95,
    6,
    99,
    2,
    9,
    99,
    103,
    2,
    9,
    103,
    107,
    1,
    5,
    107,
    111,
    1,
    111,
    5,
    115,
    1,
    115,
    13,
    119,
    1,
    13,
    119,
    123,
    2,
    6,
    123,
    127,
    1,
    5,
    127,
    131,
    1,
    9,
    131,
    135,
    1,
    135,
    9,
    139,
    2,
    139,
    6,
    143,
    1,
    143,
    5,
    147,
    2,
    147,
    6,
    151,
    1,
    5,
    151,
    155,
    2,
    6,
    155,
    159,
    1,
    159,
    2,
    163,
    1,
    9,
    163,
    0,
    99,
    2,
    0,
    14,
    0,
]


def solve1(arr):
    max_iters = math.ceil(len(arr) / 4)
    # print(f"{max_iters}")
    for i in range(max_iters):
        op_code = arr[i * 4]
        if op_code == 99:
            break
        operand1 = arr[arr[i * 4 + 1]]
        operand2 = arr[arr[i * 4 + 2]]
        dest = arr[i * 4 + 3]
        if op_code == 1:
            arr[dest] = operand1 + operand2
        elif op_code == 2:
            arr[dest] = operand1 * operand2
        else:
            print(f"Invalid op_code found. {op_code}")
            break

    return arr


def apply_before_steps(data):
    data[1] = 12
    data[2] = 2


def main(input_data):
    data = copy.copy(input_data)

    apply_before_steps(data)
    # data = [1, 0, 0, 0, 99]
    print(solve1(data))


@pytest.mark.parametrize(
    "x,y",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_solve(x, y):
    assert x == solve1(y)


if __name__ == "__main__":
    main(TEST_DATA)
