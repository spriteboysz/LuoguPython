#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:18
FileName: 入门与面试
Description:B2106 矩阵转置.py 
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    for row in zip(*grid):
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
