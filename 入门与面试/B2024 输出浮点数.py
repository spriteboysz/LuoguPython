#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:19
FileName: 入门与面试
Description:B2024 输出浮点数.py 
"""


def func():
    f = float(input().strip())
    print(f'{f:f}')
    print(f'{f:.5f}')
    print(f'{f:e}')
    print(f'{f:g}')


if __name__ == '__main__':
    func()
