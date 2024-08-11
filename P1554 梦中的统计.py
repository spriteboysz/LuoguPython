#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 15:40
FileName: 
Description:P1554 梦中的统计.py 
"""


def func():
    m, n = map(int, input().strip().split())
    digits = [0 for _ in range(10)]
    for num in range(m, n + 1):
        for ch in str(num):
            digits[int(ch)] += 1
    print(' '.join(map(str, digits)))


if __name__ == '__main__':
    func()
