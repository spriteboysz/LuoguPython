#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:42
FileName: 
Description:P8813 [CSP-J 2022] 乘方.py 
"""


def func():
    a, b = map(int, input().strip().split())
    product = 1
    for _ in range(b):
        product *= a
        if product > 10 ** 9:
            print(-1)
            return
    print(product)


if __name__ == '__main__':
    func()
