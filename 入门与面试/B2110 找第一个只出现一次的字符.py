#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:41
FileName: 入门与面试
Description:B2110 找第一个只出现一次的字符.py 
"""
from collections import defaultdict


def func():
    s = input().strip()
    cnt = defaultdict(int)
    for c in list(s):
        cnt[c] += 1
    for c in list(s):
        if cnt.get(c, 0) == 1:
            print(c)
            return
    print('no')


if __name__ == '__main__':
    func()
