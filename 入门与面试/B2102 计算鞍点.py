#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 18:49
FileName: 入门与面试
Description:B2102 计算鞍点.py 
"""


def func():
    grid = [list(map(int, input().strip().split())) for _ in range(5)]
    rows = [max(row) for row in grid]
    cols = [min(col) for col in zip(*grid)]
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == rows[i] and num == cols[j]:
                print(f'{i + 1} {j + 1} {num}')
                return
    print('not found')


if __name__ == '__main__':
    func()
