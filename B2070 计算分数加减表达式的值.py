#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:21
FileName: 入门与面试
Description:B2070 计算分数加减表达式的值.py 
"""


def func():
    n = int(input().strip())
    total = 0
    for i in range(1, n + 1):
        total += (-1) ** (i + 1) * (1 / i)
    print(f'{total:.4f}')


if __name__ == '__main__':
    func()
