#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 16:37
FileName: 
Description:B3867 [GESP202309 三级] 小杨的储蓄.py 
"""


def func():
    n, d = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    digits = [0] * n
    for i, num in enumerate(nums):
        digits[num] += (i + 1)
    print(' '.join(map(str, digits)))


if __name__ == '__main__':
    func()
