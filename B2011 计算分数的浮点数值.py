#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:31
FileName: 入门与面试
Description:B2011 计算分数的浮点数值.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(f'{a / b:.9f}')


if __name__ == '__main__':
    func()
