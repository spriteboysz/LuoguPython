#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-08 21:23
FileName: 
Description:P3717 [AHOI2017初中组] cover.py 
"""


def func():
    n, m, r = map(int, input().strip().split())
    points = [list(map(int, input().strip().split())) for _ in range(m)]
    grid = [[0] * n for _ in range(n)]
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == 1:
                continue
            for x, y in points:
                if (i - x + 1) ** 2 + (j - y + 1) ** 2<= r * r:
                    grid[i][j] = 1
                    break
    print(sum(sum(row) for row in grid))


if __name__ == '__main__':
    func()
