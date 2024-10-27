#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 23:23
FileName: P7257 [COCI2009-2010#3] FILIP
Description:
"""


def func():
    a, b = input().strip().split()
    print(max(int(a[::-1]), int(b[::-1])))


if __name__ == '__main__':
    func()
