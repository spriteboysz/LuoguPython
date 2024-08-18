#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:36
FileName: 
Description:P1634 禽兽的传染病.py 
"""


def func():
    x, n = map(int, input().strip().split())
    total = 1
    for _ in range(n):
        total += total * x
    print(total)


if __name__ == '__main__':
    func()
