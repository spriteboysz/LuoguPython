#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 09:26
FileName: 入门与面试
Description:B2091 向量点积计算.py 
"""


def func():
    _ = int(input().strip())
    v1 = list(map(int, input().strip().split()))
    v2 = list(map(int, input().strip().split()))
    print(sum([a * b for a, b in zip(v1, v2)]))


if __name__ == '__main__':
    func()
