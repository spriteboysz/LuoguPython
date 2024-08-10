#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:15
FileName: 
Description:P3954 [NOIP2017 普及组] 成绩.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    print(int(a * 0.2 + b * 0.3 + c * 0.5))


if __name__ == '__main__':
    func()
