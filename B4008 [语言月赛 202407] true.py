#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-24 22:18
FileName: 
Description:B4008 [语言月赛 202407] true.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(a // 10, b * 10, (10000 - a // 10 - b * 10))


if __name__ == '__main__':
    func()
