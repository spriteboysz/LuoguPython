#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 22:40
FileName: P9955 [USACO20DEC] Do You Know Your ABCs
Description:
"""


def func():
    nums = list(map(int, input().strip().split()))
    nums.sort()
    print(nums[0], nums[1], nums[-1] - nums[0] - nums[1])


if __name__ == '__main__':
    func()