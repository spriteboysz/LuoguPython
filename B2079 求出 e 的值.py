#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:21
FileName: 入门与面试
Description:B2079 求出 e 的值.py 
"""


def func():
    n = int(input().strip())
    total, product = 1, 1
    for i in range(1, n + 1):
        product *= i
        total += 1 / product
    print(f'{total:.10f}')


if __name__ == '__main__':
    func()
