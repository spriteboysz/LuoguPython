#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:15
FileName: 入门与面试
Description:B2006 地球人口承载力估计.py 
"""


def func():
    x, a, y, b = map(int, input().strip().split())
    print(f'{(a * x - b * y) / (a - b):.2f}')


if __name__ == '__main__':
    func()
