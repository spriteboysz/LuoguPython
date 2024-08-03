#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:01
FileName: 入门与面试
Description:B2039 整数大小比较.py 
"""


def func():
    x, y = map(int, input().strip().split())
    if x == y:
        print('=')
    else:
        print('>' if x > y else '<')


if __name__ == '__main__':
    func()
