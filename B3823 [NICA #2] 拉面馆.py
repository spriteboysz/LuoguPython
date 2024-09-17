#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:06
FileName: 
Description:B3823 [NICA #2] 拉面馆.py 
"""


def func():
    a, b, k, r, c = map(int, input().strip().split())
    print(((b - a) * k) * (r - c))


if __name__ == '__main__':
    func()
