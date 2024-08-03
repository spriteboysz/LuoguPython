#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:39
FileName: 入门与面试
Description:B2031 计算三角形面积.py 
"""


def func():
    def calc(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    x1, y1, x2, y2, x3, y3 = map(float, input().strip().split())
    a = calc(x1, y1, x2, y2)
    b = calc(x1, y1, x3, y3)
    c = calc(x2, y2, x3, y3)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'{area:.2f}')


if __name__ == '__main__':
    func()
