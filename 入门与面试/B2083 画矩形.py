#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:32
FileName: 入门与面试
Description:B2083 画矩形.py 
"""


def func():
    a, b, c, f = input().strip().split()
    a, b, f = map(int, [a, b, f])
    for i in range(a):
        if f == 1 or i == 0 or i == a - 1:
            print(c * b)
        else:
            print(c + ' ' * (b - 2) + c)


if __name__ == '__main__':
    func()
