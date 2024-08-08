#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 23:09
FileName: 入门与面试
Description:B2147 求 f(x,n).py 
"""


def func():
    def f(x, n):
        if n == 1:
            return (x + 1) ** 0.5
        else:
            return (n + f(x, n - 1)) ** 0.5

    x, n = map(float, input().strip().split())
    print(f'{f(x, n):.2f}')


if __name__ == '__main__':
    func()
