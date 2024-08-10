#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:43
FileName: 入门与面试
Description:B2134 质数的和与积.py 
"""
from functools import cache


def func():
    @cache
    def check(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    s = int(input().strip())
    maximum = -1
    for i in range(2, s):
        if check(i) and check(s - i):
            maximum = max(maximum, i * (s - i))
    print(maximum)


if __name__ == '__main__':
    func()
