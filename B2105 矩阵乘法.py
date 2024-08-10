#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:06
FileName: 入门与面试
Description:B2105 矩阵乘法.py 
"""


def func():
    n, m, k = map(int, input().strip().split())
    grid1 = [list(map(int, input().strip().split())) for _ in range(n)]
    grid2 = [list(map(int, input().strip().split())) for _ in range(m)]
    grid, row = [], []
    grid2 = list(map(lambda row: list(row), zip(*grid2)))
    for i in range(n):
        row.clear()
        for j in range(k):
            row.append(sum([a * b for a, b in zip(grid1[i], grid2[j])]))
        grid.append(row.copy())
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
