#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-23 22:00
FileName: 
Description:B3639 T2 点亮灯笼.py 
"""
import numpy


def func():
    n, m = map(int, input().split())
    arr = numpy.zeros([n], dtype=int)

    for _ in range(m):
        x = int(input()) - 1
        arr[x] ^= 1
        arr[(x - 1) % n] ^= 1
        arr[(x + 1) % n] ^= 1

    print(' '.join(map(str, arr.tolist())))


if __name__ == '__main__':
    func()
