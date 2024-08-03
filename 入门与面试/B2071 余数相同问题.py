#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:27
FileName: 入门与面试
Description:B2071 余数相同问题.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    for x in range(2, min(a, b, c)):
        if a % x == b % x == c % x:
            print(x)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
