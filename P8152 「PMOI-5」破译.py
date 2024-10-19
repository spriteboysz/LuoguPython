#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 11:04
FileName: 
Description:P8152 「PMOI-5」破译.py 
"""


def func():
    n, k = map(int, input().strip().split())
    print((n * n * k - k + 1) % 998244353)


if __name__ == '__main__':
    func()
