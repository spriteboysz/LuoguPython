#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 08:43
FileName: 主题库
Description:P1001 A+B Problem.py 
"""


def func(a, b):
    return a + b


if __name__ == '__main__':
    a, b = map(int, input().strip().split())
    print(func(a, b))
