#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:35
FileName: 入门与面试
Description:B2133 我家的门牌号.py 
"""


def func():
    n = int(input().strip())
    for b in range(1, 1000000):
        for a in range(1, b + 1):
            if (1 + b) * b // 2 - 3 * a == n:
                print(a, b)
                return
    print('Error')


if __name__ == '__main__':
    func()
