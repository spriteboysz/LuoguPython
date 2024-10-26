#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 22:57
FileName: P7174 [COCI2014-2015#4] CESTA
Description:
"""


def func():
    num = input().strip()
    if sum([int(el) for el in num]) % 3 == 0 and num.count('0') > 0:
        print(''.join(sorted(list(num))[::-1]))
    else:
        print(-1)


if __name__ == '__main__':
    func()
