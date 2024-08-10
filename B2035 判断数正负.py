#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 12:00
FileName: 入门与面试
Description:B2035 判断数正负.py 
"""


def func():
    num = int(input().strip())
    if num == 0:
        print('zero')
    else:
        print('positive' if num > 0 else 'negative')


if __name__ == '__main__':
    func()
