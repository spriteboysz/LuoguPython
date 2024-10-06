#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 10:54
FileName: 
Description:P8823 [传智杯 #3 初赛] 期末考试成绩.py 
"""


def func():
    x = int(input().strip())
    if x >= 90:
        g = 4
    elif x >= 60:
        g = 4.0 - (90 - x) * 0.1
    else:
        g = (x ** 0.5) * 10 // 1
        if g >= 60:
            g = 4.0 - (90 - g) * 0.1
        else:
            g = 0
    print(f'{g:.1f}')


if __name__ == '__main__':
    func()
