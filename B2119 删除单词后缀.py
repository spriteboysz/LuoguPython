#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:24
FileName: 入门与面试
Description:B2119 删除单词后缀.py 
"""


def func():
    s = input().strip()
    if s.endswith('er') or s.endswith('ly'):
        print(s[:-2])
    elif s.endswith('ing'):
        print(s[:-3])
    else:
        print(s)


if __name__ == '__main__':
    func()
