#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 17:44
FileName: 
Description:P6320 [COCI2006-2007#4] SIBICE.py 
"""


def func():
    n, w, h = map(int, input().strip().split())
    nums = [int(input().strip()) for _ in range(n)]
    c = (w * w + h * h) ** 0.5
    for num in nums:
        if num > c:
            print('NE')
        else:
            print('DA')


if __name__ == '__main__':
    func()
