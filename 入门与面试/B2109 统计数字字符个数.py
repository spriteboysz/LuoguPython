#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:38
FileName: 入门与面试
Description:B2109 统计数字字符个数.py 
"""


def func():
    s = input().strip()
    print(f'{sum([1 for c in list(s) if "0" <= c <= "9"])}')


if __name__ == '__main__':
    func()
