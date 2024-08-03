#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:07
FileName: 入门与面试
Description:B2042 判断一个数能否同时被 3 和 5 整除.py 
"""


def func():
    num = int(input().strip())
    print('YES' if num % 3 == 0 and num % 5 == 0 else 'NO')


if __name__ == '__main__':
    func()
