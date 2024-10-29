#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-28 23:09
FileName: P7615 [COCI2011-2012#2] OKRET
Description:
"""


def func():
    def check(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] == '.'

    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and check(i - 1, j) + check(i + 1, j) + check(i, j - 1) + check(i, j + 1) == 1:
                print(1)
                return
    print(0)


if __name__ == '__main__':
    func()
