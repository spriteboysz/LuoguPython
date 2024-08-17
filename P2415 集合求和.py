#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 10:08
FileName: 
Description:P2415 集合求和.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    print(sum(nums) * (2 ** (len(nums) - 1)))


if __name__ == '__main__':
    func()
