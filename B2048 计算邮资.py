#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:30
FileName: 入门与面试
Description:B2048 计算邮资.py 
"""
import math


def func():
    x, c = input().strip().split()
    x = int(x)
    postage = 8
    if x > 1000:
        postage += math.ceil((x - 1000) / 500) * 4
    if c == 'y':
        postage += 5
    print(postage)


if __name__ == '__main__':
    func()
