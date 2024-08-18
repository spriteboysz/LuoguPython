#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:58
FileName: 
Description:P1876 开灯.py 
"""


def func():
    n = int(input().strip())
    lights = []
    for i in range(1, n + 1):
        if i * i <= n:
            lights.append(i * i)
        else:
            break
    print(' '.join(map(str, lights)))


if __name__ == '__main__':
    func()
