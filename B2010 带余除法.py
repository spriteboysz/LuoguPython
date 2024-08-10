#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:28
FileName: 入门与面试
Description:B2010 带余除法.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(*divmod(a, b))


if __name__ == '__main__':
    func()
