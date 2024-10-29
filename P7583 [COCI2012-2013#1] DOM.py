#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 23:05
FileName: P7583 [COCI2012-2013#1] DOM
Description:
"""


def func():
    s = input().strip()
    for ch in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']:
        s = s.replace(ch, '')
    print(s)


if __name__ == '__main__':
    func()
