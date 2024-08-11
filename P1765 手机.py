#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 19:42
FileName: 
Description:P1765 手机.py 
"""
from collections import defaultdict


def func():
    s = input()
    keys = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz', ' ']
    count = defaultdict(int)
    for key in keys:
        for i, ch in enumerate(key):
            count[ch] = i + 1
    print(sum([count[ch] for ch in s]))
    print(count)


if __name__ == '__main__':
    func()
