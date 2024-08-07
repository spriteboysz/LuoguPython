#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:51
FileName: 入门与面试
Description:B2136 素数回文数的个数.py 
"""
from functools import cache


def func():
    @cache
    def check(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = int(input().strip())
    cnt = 0
    for i in range(11, n + 1):
        if check(i) and str(i) == str(i)[::-1]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
