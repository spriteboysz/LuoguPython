#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:08
FileName: 入门与面试
Description:B2043 判断能否被 3，5，7 整除.py 
"""


def func():
    x = int(input().strip())
    result = []
    for num in [3, 5, 7]:
        if x % num == 0:
            result.append(num)
    if result:
        print(' '.join(map(str, result)))
    else:
        print('n')


if __name__ == '__main__':
    func()
