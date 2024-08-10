#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:33
FileName: 入门与面试
Description:B2073 求小数的某一位.py 
"""


def func():
    a, b, n = map(int, input().strip().split())
    for _ in range(n):
        a = a % b
        a *= 10
    a = a // b
    print(a)


if __name__ == '__main__':
    func()
