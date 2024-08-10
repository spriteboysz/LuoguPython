#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:21
FileName: 
Description:P1888 三角函数.py 
"""

import math


def func():
    a, b, c = sorted(map(int, input().strip().split()))
    gcd = math.gcd(a, c)
    print(f'{a // gcd}/{c // gcd}')


if __name__ == '__main__':
    func()
