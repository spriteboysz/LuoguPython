#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:14
FileName: 入门与面试
Description:B2129 最大数 max(x,y,z).py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    m = max(a, b, c) / (max(a + b, b, c) * max(a, b, b + c))
    print(f'{m:.3f}')


if __name__ == '__main__':
    func()
