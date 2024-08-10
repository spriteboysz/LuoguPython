#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:59
FileName: 入门与面试
Description:B2054 求平均年龄.py 
"""


def func():
    n = int(input().strip())
    ages = []
    for _ in range(n):
        ages.append(int(input().strip()))
    print(f'{sum(ages) / n:.2f}')


if __name__ == '__main__':
    func()
