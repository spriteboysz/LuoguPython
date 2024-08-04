#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 15:37
FileName: 入门与面试
Description:B2100 同行列对角线的格.py 
"""


def func():
    n, a, b = map(int, input().strip().split())
    print(' '.join([f'({a},{k})' for k in range(1, n + 1)]))
    print(' '.join([f'({k},{b})' for k in range(1, n + 1)]))
    print(' '.join([f'({i + 1},{j + 1})' for i in range(n) for j in range(n) if a - b == i - j]))
    print(' '.join([f'({i},{j})' for i in range(n, 0, -1) for j in range(1, n + 1) if a + b == i + j]))


if __name__ == '__main__':
    func()
