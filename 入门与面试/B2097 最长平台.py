#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 15:16
FileName: 入门与面试
Description:B2097 最长平台.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    maximum, curr = 1, 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            curr += 1
            maximum = max(maximum, curr)
        else:
            curr = 1
    print(maximum)


if __name__ == '__main__':
    func()
