#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 18:30
FileName: 
Description:B3876 [信息与未来 2015] 中间值.py 
"""


def func():
    n = int(input().strip())
    if n % 2 == 1:
        print(n // 2 + 1)
    else:
        print(n // 2 + n // 2 + 1)


if __name__ == '__main__':
    func()
