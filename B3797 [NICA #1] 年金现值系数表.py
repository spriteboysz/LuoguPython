#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 20:10
FileName: 
Description:B3797 [NICA #1] 年金现值系数表.py 
"""


def func():
    n, i = map(int, input().strip().split())
    grid, row = [], []
    for i in range(1, i + 1):
        row.append(f'{i}%')
    grid.append(['', *row])
    for k in range(1, n + 1):
        row.clear()
        row.append(str(k))
        for j in range(1, i + 1):
            v = (1 - (1 + j / 100) ** (-k)) / (j / 100)
            row.append(f'{v:.4f}')
        grid.append(row.copy())
    for row in grid:
        print('\t'.join(row))


if __name__ == '__main__':
    func()
