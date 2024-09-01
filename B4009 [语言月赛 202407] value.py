#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-24 22:20
FileName: 
Description:B4009 [语言月赛 202407] value.py 
"""


def func():
    x, y, z, w = map(int, input().strip().split())
    for c in range(1, 1001):
        if x == z * c and y == w * c:
            print(c)
            return
    print(-1)


if __name__ == '__main__':
    func()
