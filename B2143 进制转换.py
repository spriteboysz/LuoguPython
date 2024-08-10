#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 21:08
FileName: 入门与面试
Description:B2143 进制转换.py 
"""

from string import hexdigits


def func():
    x, m = map(int, input().strip().split())
    ss = []
    while x > 0:
        x, mod = divmod(x, m)
        ss.append(mod)
    print(''.join([hexdigits[i].upper() for i in ss[::-1]]))


if __name__ == '__main__':
    func()
