#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 09:40
FileName: 
Description:B4026 [语言月赛 202409] 灵感.py 
"""


def func():
    a, b, c, d = map(int, input().strip().split())
    if c + d > a + b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
