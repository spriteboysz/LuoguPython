#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 14:57
FileName: 入门与面试
Description:B2094 不与最大数相同的数字之和.py 
"""


def func():
    n = int(input().strip())
    if n == 0:
        return 0
    nums = list(map(int, input().strip().split()))
    maximum = max(nums)
    total = 0
    for num in nums:
        if num != maximum:
            total += num
    print(total)


if __name__ == '__main__':
    func()
