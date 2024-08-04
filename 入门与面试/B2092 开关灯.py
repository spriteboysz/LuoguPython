#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 09:30
FileName: 入门与面试
Description:B2092 开关灯.py 
"""


def func():
    n = int(input().strip())
    nums = []
    for i in range(1, n + 1):
        if i * i <= n:
            nums.append(i * i)
        else:
            break
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    func()
