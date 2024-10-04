#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 10:38
FileName: 
Description:P5534 【XR-3】等差数列.py 
"""


def func():
    a1, a2, n = map(int, input().strip().split())
    an = a1 + (n - 1) * (a2 - a1)
    print((a1 + an) * n // 2)


if __name__ == '__main__':
    func()
