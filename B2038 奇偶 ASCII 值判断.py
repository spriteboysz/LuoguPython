#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 15:59
FileName: 入门与面试
Description:B2038 奇偶 ASCII 值判断.py 
"""


def func():
    ch = input().strip()
    print('YES' if ord(ch) % 2 == 1 else 'NO')


if __name__ == '__main__':
    func()
