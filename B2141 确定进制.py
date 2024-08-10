#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 21:58
FileName: 入门与面试
Description:B2141 确定进制.py 
"""


def func():
    p, q, r = input().strip().split()
    for i in range(2, 17):
        try:
            if int(p, i) * int(q, i) == int(r, i):
                print(i)
                return
        except ValueError:
            pass
    print('0')


if __name__ == '__main__':
    func()
