#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:28
FileName: 入门与面试
Description:B2132 素数对.py 
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
    for i in range(2, n - 1):
        if check(i) and check(i + 2):
            cnt += 1
            print(i, i + 2)
    if cnt == 0:
        print('empty')


if __name__ == '__main__':
    func()
