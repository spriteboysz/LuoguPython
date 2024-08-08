#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 22:44
FileName: 入门与面试
Description:B2145 digit 函数.py 
"""


def func():
    def digit(n, k):
        try:
            return str(n)[-k]
        except IndexError:
            return '0'

    import sys
    nums = []
    for line in sys.stdin:
        nums.extend(line.strip().split())
    n, k = map(int, nums)
    print(digit(n, k))


if __name__ == '__main__':
    func()
