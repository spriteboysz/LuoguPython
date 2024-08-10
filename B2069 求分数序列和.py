#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:15
FileName: 入门与面试
Description:B2069 求分数序列和.py 
"""


def func():
    n = int(input().strip())
    total, p, q = 0, 1, 2
    for i in range(n):
        total += q / p
        p, q = q, p + q
    print(f'{total:.4f}')


if __name__ == '__main__':
    func()
