#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-23 21:51
FileName: 
Description:B3638 T1 三角形面积.py 
"""


def func():
    def process(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    points = [list(map(int, input().strip().split())) for _ in range(3)]
    a, b, c = process(points[0], points[1]), process(points[0], points[2]), process(points[1], points[2])
    s = (a + b + c) * 0.5
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(round(area))


if __name__ == '__main__':
    func()
