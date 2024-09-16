#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-15 17:01
FileName: 
Description:P3742 umi的函数.py 
"""


def func():
    _ = input()
    s1, s2 = input().strip(), input().strip()
    ss = ''
    for c1, c2 in zip(s1, s2):
        if c1 < c2:
            print(-1)
            return
        ss += min(c1, c2)
    print(ss)


if __name__ == '__main__':
    func()
