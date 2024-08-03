#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:36
FileName: 入门与面试
Description:B2084 质因数分解.py 
"""


def func():
    num = int(input().strip())
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(num // i)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
