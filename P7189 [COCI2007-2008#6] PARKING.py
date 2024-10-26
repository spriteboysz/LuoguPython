#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 23:03
FileName: P7189 [COCI2007-2008#6] PARKING
Description:
"""


def func():
    a, b, c = map(int, input().strip().split())
    price = [0, a, b, c]
    grid = [list(map(int, input().strip().split())) for _ in range(3)]
    nums = [0] * 101
    for start, end in grid:
        for i in range(start, end):
            nums[i] += 1
    print(sum([price[num] * num for num in nums]))


if __name__ == '__main__':
    func()
