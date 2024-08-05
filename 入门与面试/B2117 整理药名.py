#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:20
FileName: 入门与面试
Description:B2117 整理药名.py 
"""


def func():
    n = int(input().strip())
    ss = [input().strip() for _ in range(n)]
    for s in ss:
        print(s.capitalize())


if __name__ == '__main__':
    func()
