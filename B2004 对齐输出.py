#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:01
FileName: 入门与面试
Description:B2004 对齐输出.py 
"""


def func():
    a, b, c = input().strip().split()
    print(f'{a:>8} {b:>8} {c:>8}')


if __name__ == '__main__':
    func()
    # 123456789        0       -1
    # 123456789        0       -1
