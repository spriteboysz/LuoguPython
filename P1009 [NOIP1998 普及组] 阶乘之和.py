#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 19:58
FileName: 
Description:P1009 [NOIP1998 普及组] 阶乘之和.py 
"""
from functools import lru_cache


def func():
    n = int(input().strip())

    @lru_cache
    def factorial(n):
        if n == 1:
            return n
        return factorial(n - 1) * n

    print(sum([factorial(i + 1) for i in range(n)]))


if __name__ == '__main__':
    func()
