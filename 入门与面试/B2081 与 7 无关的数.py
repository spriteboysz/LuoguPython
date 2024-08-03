#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:26
FileName: 入门与面试
Description:B2081 与 7 无关的数.py 
"""


def func():
    n = int(input().strip())
    total = 0
    for i in range(1, n + 1):
        if i % 7 == 0 or '7' in set(str(i)):
            continue
        total += i * i
    print(total)


if __name__ == '__main__':
    func()
