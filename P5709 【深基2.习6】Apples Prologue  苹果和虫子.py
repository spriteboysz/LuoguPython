#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:04
FileName: 
Description:P5709 【深基2.习6】Apples Prologue  苹果和虫子.py 
"""

import math


def func():
    m, t, s = map(int, input().strip().split())
    if t == 0:
        print('0')
    else:
        print(max(m - math.ceil(s / t), 0))


if __name__ == '__main__':
    func()
