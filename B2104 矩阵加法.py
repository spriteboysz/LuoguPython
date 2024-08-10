#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:03
FileName: 入门与面试
Description:B2104 矩阵加法.py 
"""


def func():
    n, m = map(int, input().strip().split())
    grid1 = [list(map(int, input().strip().split())) for _ in range(n)]
    grid2 = [list(map(int, input().strip().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid1[i][j] += grid2[i][j]
    for row in grid1:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
