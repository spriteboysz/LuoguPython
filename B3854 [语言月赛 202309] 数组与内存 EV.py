#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 11:46
FileName: 
Description:B3854 [语言月赛 202309] 数组与内存 EV.py 
"""


def func():
    n, m, p, q = map(int, input().strip().split())
    if p * m + q < n * m:
        print('Program ends with return value 0.')
    else:
        print('Segmentation fault.')


if __name__ == '__main__':
    func()
