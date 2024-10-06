#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 10:48
FileName: 
Description:P8822 [传智杯 #3 初赛] 课程报名.py 
"""


def func():
    n, v, m, a = map(int, input().strip().split())
    s = 0
    for i in range(n):
        if i > 0 and i % m == 0:
            v += a
        s += v
    print(s)


if __name__ == '__main__':
    func()
