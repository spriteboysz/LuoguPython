#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-07 23:21
FileName: P8071 [COCI2009-2010#7] SPAVANAC
Description:
"""


def func():
    hh, mm = map(int, input().strip().split())
    tt = hh * 60 + mm
    if tt < 45:
        tt += 24 * 60
    div, mod = divmod(tt - 45, 60)
    print(div, mod)


if __name__ == '__main__':
    func()
