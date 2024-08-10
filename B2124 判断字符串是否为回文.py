#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 22:47
FileName: 入门与面试
Description:B2124 判断字符串是否为回文.py 
"""


def func():
    s = input().strip()
    print('yes' if s == s[::-1] else 'no')


if __name__ == '__main__':
    func()
