#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-15 23:43
FileName: 
Description:P5735 【深基7.例1】距离函数.py 
"""


def func():
    def process(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    points = [list(map(float, input().strip().split())) for _ in range(3)]
    a, b, c = points
    perimeter = process(a, b) + process(a, c) + process(b, c)
    print(f'{perimeter:.2f}')


if __name__ == '__main__':
    func()
