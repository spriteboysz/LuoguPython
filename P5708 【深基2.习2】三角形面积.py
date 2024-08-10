#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:02
FileName: 
Description:P5708 【深基2.习2】三角形面积.py 
"""


def func():
    a, b, c = map(float, input().strip().split())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'{s:.1f}')


if __name__ == '__main__':
    func()
