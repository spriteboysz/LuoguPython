#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:22
FileName: 入门与面试
Description:B2108 图像模糊处理.py 
"""
from copy import deepcopy


def func():
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    grid2 = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                continue
            else:
                total = grid[i][j] + grid[i - 1][j] + grid[i + 1][j] + grid[i][j - 1] + grid[i][j + 1]
                grid2[i][j] = round(total / 5)
    for row in grid2:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
