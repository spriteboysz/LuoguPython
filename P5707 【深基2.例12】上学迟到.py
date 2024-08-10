#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:04
FileName: 
Description:P5707 【深基2.例12】上学迟到.py 
"""

import math


def func():
    s, v = map(int, input().strip().split())
    t = math.ceil(s / v)
    day = 24 * 60
    div, mod = divmod((7 * 60 + 50 - t + day) % day, 60)
    print(f'{div:02d}:{mod:02d}')


if __name__ == '__main__':
    func()
