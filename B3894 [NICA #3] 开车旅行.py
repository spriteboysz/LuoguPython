#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 16:02
FileName: 
Description:B3894 [NICA #3] 开车旅行.py 
"""


def func():
    a, b, c, d = map(float, input().strip().split())
    s = a * b + c * d
    print(f'{s:.1f}')
    print(f'{s / (b + d):.1f}')


if __name__ == '__main__':
    func()
