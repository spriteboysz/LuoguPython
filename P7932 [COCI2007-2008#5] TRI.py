#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-31 23:06
FileName: P7932 [COCI2007-2008#5] TRI
Description:
"""


def func():
    a, b, c = map(int, input().strip().split())
    if a + b == c:
        print(f'{a}+{b}={c}')
    elif a == b + c:
        print(f'{a}={b}+{c}')
    elif a - b == c:
        print(f'{a}-{b}={c}')
    elif a == b - c:
        print(f'{a}={b}-{c}')
    elif a * b == c:
        print(f'{a}*{b}={c}')
    elif a == b * c:
        print(f'{a}={b}*{c}')
    elif a // b == c:
        print(f'{a}/{b}={c}')
    elif a == b // c:
        print(f'{a}={b}/{c}')
    else:
        print('Error')


if __name__ == '__main__':
    func()
