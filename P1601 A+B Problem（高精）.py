#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 11:22
FileName: 
Description:P1601 A+B Problem（高精）.py 
"""


def func():
    a = input().strip()
    b = input().strip()
    c, carry = '', 0
    while a or b or carry:
        a1, b1 = 0, 0
        if a:
            a1 = int(a[-1])
            a = a[:-1]
        if b:
            b1 = int(b[-1])
            b = b[:-1]
        carry, mod = divmod(a1 + b1 + carry, 10)
        c += str(mod)
    print(c[::-1])


if __name__ == '__main__':
    func()
