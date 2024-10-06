#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:35
FileName: 
Description:P8839 [传智杯 #4 初赛] 组原成绩.py 
"""
import math


def func():
    t, h, e = map(int, input().strip().split())
    print(math.floor(t * 0.2 + h * 0.3 + e * 0.5))


if __name__ == '__main__':
    func()
