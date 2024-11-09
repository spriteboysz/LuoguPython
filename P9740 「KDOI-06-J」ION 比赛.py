#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 23:16
FileName: P9740 「KDOI-06-J」ION 比赛
Description:
"""

import math


def func():
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    t = int(input().strip())
    curr = 0
    for a, b in data:
        curr += 100 // a * b
    if curr >= t:
        print('Already Au.')
        return
    diff = t - curr
    for a, b in data:
        curr = 100 // a * b
        if diff > 100 - curr:
            print('NaN')
        else:
            print(math.ceil(diff / (100 // a)))


if __name__ == '__main__':
    func()
