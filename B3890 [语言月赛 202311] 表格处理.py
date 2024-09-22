#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 14:07
FileName: 
Description:B3890 [语言月赛 202311] 表格处理.py 
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(2 * n)]
    for i in range(2 * n):
        for j in range(0, 2 * m, 2):
            grid[i][j] += grid[i][j + 1]
    for i in range(0, 2 * n, 2):
        for j in range(2 * m):
            grid[i][j] += grid[i + 1][j]
    grid = [list(x) for x in zip(*grid[::2])][::2]
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
