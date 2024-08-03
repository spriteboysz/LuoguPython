#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:26
FileName: 入门与面试
Description:B2063 人口增长问题.py 
"""


def func():
    x, n = map(int, input().strip().split())
    print(f'{x * (1 + 0.001) ** n:.4f}')


if __name__ == '__main__':
    func()
