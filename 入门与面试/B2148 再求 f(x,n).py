#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 23:13
FileName: 入门与面试
Description:B2148 再求 f(x,n).py 
"""


def func():
    def f(x, n):
        if n == 1:
            return x / (1 + x)
        else:
            return x / (n + f(x, n - 1))

    x, n = float(input().strip()), int(input().strip())
    print(f'{f(x, n):.2f}')


if __name__ == '__main__':
    func()
