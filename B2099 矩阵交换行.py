#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 15:33
FileName: 入门与面试
Description:B2099 矩阵交换行.py 
"""


def func():
    grid = [list(map(int, input().strip().split())) for _ in range(5)]
    m, n = map(int, input().strip().split())
    grid[m - 1], grid[n - 1] = grid[n - 1], grid[m - 1]
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
