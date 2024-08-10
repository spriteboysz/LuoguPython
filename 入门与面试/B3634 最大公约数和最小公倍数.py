#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 10:00
FileName: 入门与面试
Description:B3634 最大公约数和最小公倍数.py 
"""
import math


def func():
    a, b = map(int, input().strip().split())
    print(math.gcd(a, b), math.lcm(a, b))


if __name__ == '__main__':
    func()
