#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:41
FileName: 入门与面试
Description:B2085 第 n 小的质数.py 
"""


def func():
    def check(x):
        if x < 2:
            return False;
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    n = int(input().strip())
    for i in range(2, 10 ** 15):
        if check(i):
            n = n - 1
        if n == 0:
            print(i)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
