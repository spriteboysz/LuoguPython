#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 11:11
FileName: 
Description:P2670 [NOIP2015 普及组] 扫雷游戏.py 
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '?':
                num = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < n and 0 <= j + dy < m and grid[i + dx][j + dy] == '*':
                            num += 1
                grid[i][j] = str(num)

    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    func()
