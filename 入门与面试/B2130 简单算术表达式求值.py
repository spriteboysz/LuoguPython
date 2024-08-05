#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:17
FileName: 入门与面试
Description:B2130 简单算术表达式求值.py 
"""


def func():
    s = input().strip()
    process = {'+': lambda a, b: a + b,
               '-': lambda a, b: a - b,
               '*': lambda a, b: a * b,
               '/': lambda a, b: a//b,
               '%': lambda a, b: a % b
               }
    for k, v in process.items():
        if k in s:
            a, b = map(int, s.split(k))
            print(v(a, b))
            return
    print('Error')


if __name__ == '__main__':
    func()
