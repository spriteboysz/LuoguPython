#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:10
FileName: 入门与面试
Description:B2128 素数个数.py 
"""


def func():
    def check(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = int(input().strip())
    print(len(list(filter(check, range(2, n + 1)))))


if __name__ == '__main__':
    func()
