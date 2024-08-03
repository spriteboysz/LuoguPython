#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:23
FileName: 入门与面试
Description:B2025 输出字符菱形.py 
"""


def func():
    for i in range(-2, 3):
        print(str.center('*' * (abs(abs(i) - 2) * 2 + 1), 5))


if __name__ == '__main__':
    func()
