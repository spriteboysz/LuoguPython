#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 23:17
FileName: 
Description:P1598 垂直柱状图.py 
"""

from itertools import zip_longest


def func():
    s = ''.join([input().strip() for _ in range(4)])
    alphabet = [0] * 26
    for ch in s:
        if 'A' <= ch <= 'Z':
            alphabet[ord(ch) - ord('A')] += 1

    grid = []
    for i in range(26):
        grid.append(list(f'{chr(ord("A") + i)}' + '*' * alphabet[i]))

    grid = list(map(lambda row: list(row), zip_longest(*grid)))
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if not num:
                grid[i][j] = ' '
    for row in grid[::-1]:
        print(' '.join(row).rstrip())


if __name__ == '__main__':
    func()
