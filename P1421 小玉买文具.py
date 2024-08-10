#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:14
FileName: 
Description:P1421 小玉买文具.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(((10 * a) + b) // 19)


if __name__ == '__main__':
    func()
