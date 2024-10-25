#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-25 20:47
FileName: P6489 [COCI2010-2011#6] USPON
Description:
"""


def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    maximum, acc = 0, 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            acc += (nums[i] - nums[i - 1])
        else:
            maximum = max(maximum, acc)
            acc = 0
    print(max(maximum, acc))


if __name__ == '__main__':
    func()
