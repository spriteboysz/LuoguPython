#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 09:56
FileName: P8295 [COCI2012-2013#2] MORTADELA
Description:
"""


def func():
    x, y = map(int, input().strip().split())
    n = int(input().strip())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    prices = []
    for x1, y1 in grid:
        prices.append(x1 * 1000 / y1)
    prices.append(x * 1000 / y)
    print(f'{min(prices):.2f}')


if __name__ == '__main__':
    func()
