#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:15
FileName: 入门与面试
Description:B2059 奇数求和.py 
"""


def func():
    m, n = map(int, input().strip().split())
    total = 0
    for num in range(m, n + 1):
        if num % 2 == 1:
            total += num
    print(total)


if __name__ == '__main__':
    func()
