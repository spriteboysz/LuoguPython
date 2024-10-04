#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:01
FileName: 
Description:P8706 [蓝桥杯 2020 省 AB1] 解码.py 
"""


def func():
    s = input().strip()
    ss = ''
    for i, c in enumerate(s):
        if '0' <= c <= '9':
            ss += s[i - 1] * (int(c) - 1)
        else:
            ss += c
    print(ss)


if __name__ == '__main__':
    func()
