#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:13
FileName: 入门与面试
Description:B2022 输出保留 12 位小数的浮点数.py 
"""


def func():
    f = float(input().strip())
    print(f'{f - 0.000000000000001:.12f}')


if __name__ == '__main__':
    func()
