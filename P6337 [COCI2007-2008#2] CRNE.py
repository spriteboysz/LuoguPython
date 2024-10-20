#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-20 08:32
FileName: 
Description:P6337 [COCI2007-2008#2] CRNE.py 
"""


def func():
    n = int(input().strip())
    if n % 2 == 0:
        a = b = n // 2
    else:
        a = n // 2
        b = a + 1
    print((a + 1) * (b + 1))


if __name__ == '__main__':
    func()
