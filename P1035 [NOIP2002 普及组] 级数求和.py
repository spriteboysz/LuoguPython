#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 21:25
FileName: 
Description:P1035 [NOIP2002 普及组] 级数求和.py 
"""


def func():
    k = int(input().strip())
    total, i = 0, 1
    while total <= k:
        total += 1 / i
        i += 1
    print(i - 1)


if __name__ == '__main__':
    func()
