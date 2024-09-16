#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 19:43
FileName: 
Description:B3793 [NICA #1] 自动取款机.py 
"""
import math


def func():
    a, b = map(int, input().strip().split())
    if a <= b:
        print(0)
    else:
        print(math.ceil((a - b) / 100))


if __name__ == '__main__':
    func()
