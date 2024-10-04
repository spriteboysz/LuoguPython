#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 10:56
FileName: 
Description:P8680 [蓝桥杯 2019 省 B] 特别数的和.py 
"""


def func():
    n = int(input().strip())
    print(sum([i for i in range(1, n + 1) if set(str(i)) & {'2', '0', '1', '9'}]))


if __name__ == '__main__':
    func()
