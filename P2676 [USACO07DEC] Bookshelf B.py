#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 14:46
FileName: 
Description:P2676 [USACO07DEC] Bookshelf B.py 
"""


def func():
    n, high = map(int, input().strip().split())
    data = [int(input().strip()) for _ in range(n)]
    acc = 0
    for i, num in enumerate(sorted(data, reverse=True)):
        acc += num
        if acc >= high:
            print(i + 1)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
