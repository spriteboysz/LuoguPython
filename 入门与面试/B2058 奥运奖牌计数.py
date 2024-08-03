#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:10
FileName: 入门与面试
Description:B2058 奥运奖牌计数.py 
"""


def func():
    n = int(input().strip())
    a, b, c = 0, 0, 0
    for i in range(n):
        a1, b1, c1 = map(int, input().strip().split())
        a += a1
        b += b1
        c += c1
    print(a, b, c, sum([a, b, c]))


if __name__ == '__main__':
    func()
