#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:38
FileName: 
Description:P8840 [传智杯 #4 初赛] 报告赋分.py 
"""


def func():
    t = int(input().strip())
    grid = [map(int, input().strip().split()) for _ in range(t)]
    for a, p in grid:
        if p < 16:
            a -= 10
        elif p > 20:
            a -= p - 20
        print(max(0, a))


if __name__ == '__main__':
    func()
