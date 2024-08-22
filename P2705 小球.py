#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-22 22:57
FileName: 
Description:P2705 小球.py 
"""
import math

def func():
    r, b, c, d, e = map(int, input().strip().split())
    maximum = -math.inf
    for i in range(min(r, b) + 1):
        s = c * (r - i) + d * (b - i) + i * e * 2
        maximum = max(maximum, s)
    print(maximum)


if __name__ == '__main__':
    func()
