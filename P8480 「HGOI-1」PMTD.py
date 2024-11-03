#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 21:15
FileName: P8480 「HGOI-1」PMTD
Description:
"""

import math


def func():
    n, m = map(int, input().strip().split())
    nums = map(int, input().strip().split())
    maximum, minimum = -1, math.inf
    for num in nums:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    if maximum < 2:
        maximum = (maximum + 2) * (2 ** (m - 1))
    else:
        maximum = maximum * (2 ** m)
    print(maximum - minimum)


if __name__ == '__main__':
    func()
