#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:12
FileName: 入门与面试
Description:B2076 球弹跳高度的计算.py 
"""


def func():
    h = int(input().strip())
    total = h
    for i in range(9):
        total += h
        h /= 2
    print(total)
    print(h / 2)


if __name__ == '__main__':
    func()
