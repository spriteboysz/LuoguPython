#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 16:36
FileName: 
Description:B4025 最大公约数.py 
"""
import math


def func():
    a, b = map(int, input().strip().split())
    print(math.gcd(a, b))


if __name__ == '__main__':
    func()
