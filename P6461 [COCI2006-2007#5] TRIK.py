#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-25 20:58
FileName: P6461 [COCI2006-2007#5] TRIK
Description:
"""


def func():
    s = input().strip()
    a, b, c = 1, 0, 0
    for ch in s:
        if ch == 'A' and a + b == 1:
            a, b = b, a
        elif ch == 'B' and b + c == 1:
            b, c = c, b
        elif ch == 'C' and a + c == 1:
            a, c = c, a
    print([a, b, c].index(1) + 1)


if __name__ == '__main__':
    func()
