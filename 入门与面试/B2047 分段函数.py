#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:26
FileName: 入门与面试
Description:B2047 分段函数.py 
"""


def func():
    x = float(input().strip())
    if 0 <= x < 5:
        y = 2.5 - x
    elif 5 <= x < 10:
        y = 2 - 1.5 * (x - 3) * (x - 3)
    elif 10 <= x < 20:
        y = x / 2 - 1.5
    else:
        raise ValueError('input error')
    print(f'{y:.3f}')


if __name__ == '__main__':
    func()
