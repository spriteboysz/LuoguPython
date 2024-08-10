#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:41
FileName: 入门与面试
Description:B2015 计算并联电阻的阻值.py 
"""


def func():
    r1, r2 = map(float, input().strip().split())
    print(f'{r1 * r2 / (r1 + r2):.2f}')


if __name__ == '__main__':
    func()
