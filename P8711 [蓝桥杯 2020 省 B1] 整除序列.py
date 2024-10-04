#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:06
FileName: 
Description:P8711 [蓝桥杯 2020 省 B1] 整除序列.py 
"""


def func():
    n = int(input().strip())
    nums = []
    while n > 0:
        nums.append(n)
        n //= 2
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    func()
