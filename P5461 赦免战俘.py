#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-16 21:10
FileName: 
Description:P5461 赦免战俘.py 
"""


def func():
    def process(x, y, n):
        if n == 0:
            return
        for i in range(x, x + n // 2):
            for j in range(y, y + n // 2):
                grid[i][j] = 0
        process(x, y + n // 2, n // 2)
        process(x + n // 2, y, n // 2)
        process(x + n // 2, y + n // 2, n // 2)

    n = int(input().strip())
    grid = [[1] * (2 ** n) for _ in range(2 ** n)]
    process(0, 0, 2 ** n)
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    func()
