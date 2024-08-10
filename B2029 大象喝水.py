#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:32
FileName: 入门与面试
Description:B2029 大象喝水.py 
"""

import math


def func():
    h, r = map(int, input().strip().split())
    print(math.ceil(20 * 1000 / (3.14 * r ** 2 * h)))


if __name__ == '__main__':
    func()
