#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-24 23:44
FileName: P6500 [COCI2010-2011#3] ZBROJ
Description:
"""


def func():
    a, b = input().strip().split()
    a1, b1 = int(a.replace('6', '5')), int(b.replace('6', '5'))
    a2, b2 = int(a.replace('5', '6')), int(b.replace('5', '6'))
    print(a1 + b1, a2 + b2)


if __name__ == '__main__':
    func()
