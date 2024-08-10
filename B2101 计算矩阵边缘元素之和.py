#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 16:11
FileName: 入门与面试
Description:B2101 计算矩阵边缘元素之和.py 
"""


def func():
    m, n = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(m)]
    total = 0
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                total += num
    print(total)


if __name__ == '__main__':
    func()
