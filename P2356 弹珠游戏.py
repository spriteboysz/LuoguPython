#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 15:30
FileName: 
Description:P2356 弹珠游戏.py 
"""


def func():
    n = int(input().strip())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    rows, cols = [0 for _ in range(n)], [0 for _ in range(n)]
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            rows[i] += num
            cols[j] += num
    maximum = 0
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == 0:
                maximum = max(maximum, rows[i] + cols[j])
    print(maximum)


if __name__ == '__main__':
    func()
