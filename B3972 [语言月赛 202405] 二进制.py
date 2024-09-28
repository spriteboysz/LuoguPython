#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 10:39
FileName: 
Description:B3972 [语言月赛 202405] 二进制.py 
"""


def func():
    n = int(input().strip())
    while n > 0:
        n, mod = divmod(n, 2)
        print(n, mod)


if __name__ == '__main__':
    func()
