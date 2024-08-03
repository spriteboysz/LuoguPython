#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:27
FileName: 入门与面试
Description:B2009 计算 (a+b) c 的值.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    print((a + b) // c)


if __name__ == '__main__':
    func()
