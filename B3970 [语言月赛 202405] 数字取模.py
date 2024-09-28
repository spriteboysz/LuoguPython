#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 09:10
FileName: 
Description:B3970 [语言月赛 202405] 数字取模.py 
"""


def func():
    x, k = map(int, input().strip().split())
    print(int(''.join([str(int(c) % k) for c in str(x)])))


if __name__ == '__main__':
    func()
