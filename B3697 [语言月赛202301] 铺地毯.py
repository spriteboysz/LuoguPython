#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 22:29
FileName: 
Description:B3697 [语言月赛202301] 铺地毯.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    if a % c != 0 or b % c != 0:
        print(-1)
    else:
        print((a // c) * (b // c))


if __name__ == '__main__':
    func()
