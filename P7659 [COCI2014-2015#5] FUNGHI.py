#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-30 21:08
FileName: P7659 [COCI2014-2015#5] FUNGHI
Description:
"""


def func():
    nums = [int(input().strip()) for _ in range(8)] * 2
    print(max([sum(nums[i:i + 4]) for i in range(len(nums) - 4)]))


if __name__ == '__main__':
    func()
