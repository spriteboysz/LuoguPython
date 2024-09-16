#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 20:35
FileName: 
Description:B3806 [语言月赛 202307] 枚举结构.py 
"""
from string import ascii_lowercase


def func():
    x, y, z, w = input().strip().split()
    if x != z or x not in ascii_lowercase:
        print('Invalid')
        print(-1)
    else:
        print('valid')
        print(abs(int(y) - int(w)) + 1)


if __name__ == '__main__':
    func()
