#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-22 23:25
FileName: 
Description:P2907 [USACO08OPEN] Roads Around The Farm S.py 
"""


def func():
    def process(n):
        if n - k > 0 and (n - k) % 2 == 0:
            return process((n + k) // 2) + process((n - k) // 2)
        return 1

    n, k = map(int, input().strip().split())
    print(process(n))


if __name__ == '__main__':
    func()
