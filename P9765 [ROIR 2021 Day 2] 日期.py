#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 23:05
FileName: P9765 [ROIR 2021 Day 2] 日期
Description:
"""

from string import ascii_lowercase


def func():
    d, m, w = map(int, input().strip().split())
    i, j, k = map(int, input().strip().split())
    days = (k - 1) * (m * d) + (j - 1) * d + i
    print(ascii_lowercase[((days-1) % w)])


if __name__ == '__main__':
    func()
