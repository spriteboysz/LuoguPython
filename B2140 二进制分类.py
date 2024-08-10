#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 22:10
FileName: 入门与面试
Description:B2140 二进制分类.py 
"""


def func():
    n = int(input().strip())
    cnt = 0
    for i in range(1, n + 1):
        ss = bin(i)[2:]
        if ss.count('1') > ss.count('0'):
            cnt += 1
    print(f'{cnt} {n - cnt}')


if __name__ == '__main__':
    func()
