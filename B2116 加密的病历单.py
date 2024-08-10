#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:08
FileName: 入门与面试
Description:B2116 加密的病历单.py 
"""


def func():
    s = input().strip()
    s = s.swapcase()[::-1]
    ss = []
    table = {k: v for k, v in zip('xyzXYZ', 'abcABC')}
    for c in s:
        if c in table:
            ss.append(table.get(c))
        else:
            ss.append(chr(ord(c) + 3))
    print(''.join(ss))


if __name__ == '__main__':
    func()
