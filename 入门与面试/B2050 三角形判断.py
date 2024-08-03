#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:38
FileName: 入门与面试
Description:B2050 三角形判断.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    nums.sort()
    print(1 if sum(nums[:2]) > nums[-1] else 0)


if __name__ == '__main__':
    func()
