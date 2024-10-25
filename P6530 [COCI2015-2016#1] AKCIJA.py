#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-24 23:25
FileName: P6530 [COCI2015-2016#1] AKCIJA
Description:
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    nums.sort(reverse=True)
    print(sum(nums) - sum(nums[2::3]))


if __name__ == '__main__':
    func()
