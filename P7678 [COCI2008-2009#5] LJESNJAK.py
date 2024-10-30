#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-30 21:19
FileName: P7678 [COCI2008-2009#5] LJESNJAK
Description:
"""


def func():
    s = input().strip()
    for c in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
        s = s.replace(c, '*')
    print(len(s))


if __name__ == '__main__':
    func()
