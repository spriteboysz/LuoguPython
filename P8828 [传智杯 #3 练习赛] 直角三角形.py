#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:10
FileName: 
Description:P8828 [传智杯 #3 练习赛] 直角三角形.py 
"""


def func():
    c = int(input().strip())
    for a in range(1, c):
        if (b := (c * c - a * a) ** 0.5) % 1 == 0:
            print(a, int(b))
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
