#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:37
FileName: 入门与面试
Description:B2030 计算线段长度.py 
"""


def func():
    x1, y1 = map(int, input().strip().split())
    x2, y2 = map(int, input().strip().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(f'{distance:.3f}')


if __name__ == '__main__':
    func()
