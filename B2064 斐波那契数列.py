#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:30
FileName: 入门与面试
Description:B2064 斐波那契数列.py 
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    f = [1, 1]
    while len(f) <= max(nums):
        f.append(f[-1] + f[-2])

    for num in nums:
        print(f[num - 1])


if __name__ == '__main__':
    func()
