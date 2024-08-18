#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 15:35
FileName: 
Description:P2393 yyy loves Maths II.py 
"""

from decimal import Decimal


def func():
    try:
        s = input().strip().split()
        print(f'{sum([Decimal(num) for num in s]):.5f}')
    except EOFError:
        print("0.00000")


if __name__ == '__main__':
    func()
