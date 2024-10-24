#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 22:16
FileName: P6832 [Cnoi2020] 子弦
Description:
"""

from collections import Counter


def func():
    s = input().strip()
    print(max(Counter(s).values()))


if __name__ == '__main__':
    func()
