#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:42
FileName: 
Description:P1639 [USACO18FEB] Teleportation B.py 
"""


def func():
    a, b, x, y = map(int, input().strip().split())
    a, b = sorted([a, b])
    x, y = sorted([x, y])
    print(min(abs(a - x) + abs(b - y), b - a))


if __name__ == '__main__':
    func()
