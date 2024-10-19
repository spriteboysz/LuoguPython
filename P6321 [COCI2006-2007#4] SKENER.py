#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 17:55
FileName: 
Description:P6321 [COCI2006-2007#4] SKENER.py 
"""


def func():
    r, c, zr, zc = map(int, input().strip().split())
    grid1 = [list(input().strip()) for _ in range(r)]
    grid2 = [[''] * zc * c for _ in range(zr * r)]
    for i, row in enumerate(grid1):
        for j, char in enumerate(row):
            for m in range(i * zr, i * zr + zr):
                for n in range(j * zc, j * zc + zc):
                    grid2[m][n] = char
    for row in grid2:
        print(''.join(row))


if __name__ == '__main__':
    func()
