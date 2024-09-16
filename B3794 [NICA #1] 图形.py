#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 19:54
FileName: 
Description:B3794 [NICA #1] 图形.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    pi = 3.1415926535
    area = (a + c) * (b + c) - c * c + pi * c * c / 4
    print(f'{area / 10000:.3f}')


if __name__ == '__main__':
    func()
