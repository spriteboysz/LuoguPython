#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:09
FileName: 入门与面试
Description:B2075 幂的末尾.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(f'{a ** b % 1000:03d}')


if __name__ == '__main__':
    func()
