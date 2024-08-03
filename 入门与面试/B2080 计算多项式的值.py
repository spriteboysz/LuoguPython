#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:24
FileName: 入门与面试
Description:B2080 计算多项式的值.py 
"""


def func():
    x, n = map(float, input().strip().split())
    total = 0
    for i in range(int(n) + 1):
        total += x ** i
    print(f'{total:.2f}')


if __name__ == '__main__':
    func()
