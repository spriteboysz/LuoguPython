#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:46
FileName: 入门与面试
Description:B2086 不定方程求解.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    cnt = 0
    for x in range(0, 1001):
        for y in range(0, 1001):
            if a * x + b * y == c:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
