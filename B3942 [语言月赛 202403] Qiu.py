#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 10:53
FileName: 
Description:B3942 [语言月赛 202403] Qiu.py 
"""

import math


def func():
    n, k, p, q = map(int, input().strip().split())
    print(max(0, math.ceil(q * k / p) - n))


if __name__ == '__main__':
    func()
