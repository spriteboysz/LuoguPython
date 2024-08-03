#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:19
FileName: 入门与面试
Description:B2078 含 k 个 3 的数.py 
"""


def func():
    m, k = map(int, input().strip().split())
    print('YES' if list(str(m)).count('3') == k else 'NO')


if __name__ == '__main__':
    func()
