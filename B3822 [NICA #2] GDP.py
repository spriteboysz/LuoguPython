#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:04
FileName: 
Description:B3822 [NICA #2] GDP.py 
"""


def func():
    c, i, g, m, x = map(float, input().strip().split())
    print(f'{c + i + g + x - m:.2f}')


if __name__ == '__main__':
    func()
