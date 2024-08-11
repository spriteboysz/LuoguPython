#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 13:58
FileName: 
Description:P2615 [NOIP2015 提高组] 神奇的幻方.py 
"""


def func():
    n = int(input().strip())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, n // 2
    grid[x][y] = 1
    for i in range(2, n * n + 1):
        if x == 0 and y != n - 1:
            x, y = n - 1, y + 1
        elif x != 0 and y == n - 1:
            x, y = x - 1, 0
        elif x == 0 and y == n - 1:
            x += 1
        elif x != 0 and y != n - 1:
            if grid[x - 1][y + 1] == 0:
                x, y = x - 1, y + 1
            else:
                x += 1
        else:
            break
        grid[x][y] = i
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
