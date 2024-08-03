#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:18
FileName: 入门与面试
Description:B2060 满足条件的数累加.py 
"""


def func():
    m, n = map(int, input().strip().split())
    total = 0
    for num in range(m, n + 1):
        if num % 17 == 0:
            total += num
    print(total)


if __name__ == '__main__':
    func()
