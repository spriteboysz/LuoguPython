#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:56
FileName: 入门与面试
Description:B2032 等差数列末项计算.py 
"""


def func():
    a1, a2, n = map(int, input().strip().split())
    print(a1 + (n - 1) * (a2 - a1))


if __name__ == '__main__':
    func()
