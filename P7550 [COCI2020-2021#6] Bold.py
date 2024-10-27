#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 22:23
FileName: P7550 [COCI2020-2021#6] Bold
Description:
"""


def func():
    n, m = map(int, input().strip().split())
    grid1 = [list(input().strip()) for _ in range(n)]
    grid2 = [['.'] * m for _ in range(n)]
    for i, row in enumerate(grid1):
        for j, ch in enumerate(row):
            if ch == '#':
                grid2[i][j] = '#'
                grid2[i][min(m, j + 1)] = '#'
                grid2[min(n, i + 1)][j] = '#'
                grid2[min(n, i + 1)][min(m, j + 1)] = '#'

    for row in grid2:
        print(''.join(row))


if __name__ == '__main__':
    func()
