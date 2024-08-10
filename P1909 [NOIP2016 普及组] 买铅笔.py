#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:48
FileName: 
Description:P1909 [NOIP2016 普及组] 买铅笔.py 
"""
from math import inf, ceil


def func():
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(3)]
    minimum = inf
    for c, p in data:
        minimum = min(minimum, ceil(n / c) * p)
    print(minimum)


if __name__ == '__main__':
    func()
