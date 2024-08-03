#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:22
FileName: 入门与面试
Description:B2046 骑车与走路.py 
"""


def func():
    s = int(input().strip())
    a, b = s / 3 + 50, s / 1.2
    if a == b:
        print('All')
    else:
        print('Bike' if a < b else 'Walk')


if __name__ == '__main__':
    func()
