#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 22:40
FileName: 入门与面试
Description:B2144 阿克曼（Ackermann）函数.py 
"""


def func():
    def ackermann(m, n):
        if m == 0:
            return n + 1
        elif n == 0 and m > 0:
            return ackermann(m - 1, 1)
        elif m > 0 and n > 0:
            return ackermann(m - 1, ackermann(m, n - 1))
        else:
            raise ValueError('Error')

    m, n = map(int, input().strip().split())
    print(ackermann(m, n))


if __name__ == '__main__':
    func()
