#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:55
FileName: 入门与面试
Description:B2020 分糖果.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    cnt, n = 0, len(nums)
    for i, num in enumerate(nums):
        div, mod = divmod(num, 3)
        cnt += mod
        nums[i] = div
        nums[i - 1] += div
        nums[(i + 1) % n] += div
    print(' '.join(map(str, nums)))
    print(cnt)


if __name__ == '__main__':
    func()
