#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 18:10
FileName: P8242 [COCI2013-2014#3] OKVIR
Description:
"""

def func():
    m, n = map(int, input().strip().split())
    u, l, r, d = map(int, input().strip().split())
    grid1 = [input().strip() for _ in range(m)]
    m2, n2 = m + u + d, n + r + l
    grid2 = [['#'] * n2 for _ in range(m2)]
    for i in range(m2):
        for j in range(n2):
            if (i + j) % 2 == 1:
                grid2[i][j] = '.'
    for i in range(u, m + u):
        for j in range(l, n + l):
            grid2[i][j] = grid1[i - u][j - l]

    for row in grid2:
        print(''.join(row))


if __name__ == '__main__':
    func()
