#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:56
FileName: 入门与面试
Description:B2113 输出亲朋字符串.py 
"""


def func():
    s = input().strip()
    s = s + s[0]
    ss = [chr(ord(s[i - 1]) + ord(s[i])) for i in range(1, len(s))]
    print(''.join(ss))


if __name__ == '__main__':
    func()
