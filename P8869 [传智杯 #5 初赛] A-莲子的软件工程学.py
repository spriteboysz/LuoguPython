#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:49
FileName: 
Description:P8869 [传智杯 #5 初赛] A-莲子的软件工程学.py 
"""


def func():
    a, b = map(int, input().strip().split())
    if b < 0:
        print(-abs(a))
    else:
        print(abs(a))


if __name__ == '__main__':
    func()
