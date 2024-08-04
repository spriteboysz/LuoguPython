#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 15:10
FileName: 入门与面试
Description:B2096 直方图.py 
"""
from collections import defaultdict


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    maximum = max(nums)
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    for num in range(maximum + 1):
        print(count.get(num, 0))


if __name__ == '__main__':
    func()
