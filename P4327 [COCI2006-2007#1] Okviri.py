#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 10:06
FileName: 
Description:P4327 [COCI2006-2007#1] Okviri.py 
"""


def func():
    s = input().strip()
    n = len(s)
    m = n * 5 - (n - 1)
    grid = [['.'] * m for _ in range(5)]
    for i in range(2, m, 4):
        grid[0][i] = '#'
        grid[-1][i] = '#'
    for i in range(1, m, 2):
        grid[1][i] = '#'
        grid[-2][i] = '#'
    for i in range(0, m, 4):
        grid[2][i] = '#'
    for i in range(2, m, 4):
        grid[2][i] = s[0]
        s = s[1:]
    for i in range(10, m, 12):
        grid[0][i] = '*'
        grid[-1][i] = '*'
    for i in range(9, m, 12):
        grid[1][i] = '*'
        grid[1][i + 2] = '*'
        grid[-2][i] = '*'
        grid[-2][i + 2] = '*'
    for i in range(8, m - 1, 12):
        grid[2][i] = '*'
        grid[2][i + 4] = '*'

    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    func()
