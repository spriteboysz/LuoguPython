#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 21:54
FileName: P8044 [COCI2015-2016#4] YODA
Description:
"""
from itertools import zip_longest


def func():
    num1 = list(input().strip())
    num2 = list(input().strip())
    num3, num4 = [], []
    for a, b in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
        if int(a) > int(b):
            num3.append(a)
        elif int(a) < int(b):
            num4.append(b)
        else:
            num3.append(a)
            num4.append(b)
    print(int(''.join(num3[::-1])) if num3 else 'YODA')
    print(int(''.join(num4[::-1])) if num4 else 'YODA')


if __name__ == '__main__':
    func()
