#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 23:06
FileName: 入门与面试
Description:B2146 Hermite 多项式.py 
"""


def func():
    def hermite(x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x * 2
        else:
            return 2 * x * hermite(x, n - 1) - 2 * (n - 1) * hermite(x, n - 2)

    n, x = map(int, input().strip().split())
    print(hermite(x, n))


if __name__ == '__main__':
    func()
