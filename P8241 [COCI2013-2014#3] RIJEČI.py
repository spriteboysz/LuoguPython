#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 20:26
FileName: P8241 [COCI2013-2014#3] RIJEČI
Description:
"""


def func():
    k = int(input().strip())
    a0, a1 = 0, 1
    for _ in range(k - 1):
        a0, a1 = a1, a0 + a1
    print(a0, a1)


if __name__ == '__main__':
    func()
