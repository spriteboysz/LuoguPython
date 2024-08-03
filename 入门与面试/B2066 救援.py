#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:56
FileName: 入门与面试
Description:B2066 救援.py 
"""
import math


def func():
    n = int(input().strip())
    records = [list(map(float, input().strip().split())) for _ in range(n)]
    total = 0
    for x, y, n in records:
        total += (x * x + y * y) ** 0.5 * 2 / 50
        total += 1.5 * n
    print(math.ceil(total))


if __name__ == '__main__':
    func()
