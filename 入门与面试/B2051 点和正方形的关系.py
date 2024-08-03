#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:41
FileName: 入门与面试
Description:B2051 点和正方形的关系.py 
"""


def func():
    x, y = map(int, input().strip().split())
    print('yes' if -1 <= x <= 1 and -1 <= y <= 1 else 'no')


if __name__ == '__main__':
    func()
