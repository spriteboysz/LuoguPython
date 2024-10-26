#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 22:48
FileName: P7018 [CERC2013] Bus
Description:
"""


def func():
    nums = [0]
    for i in range(31):
        nums.append(nums[-1] * 2 + 1)

    n = int(input())
    nums1 = [int(input()) for _ in range(n)]
    for num in nums1:
        print(nums[num])


if __name__ == '__main__':
    func()
