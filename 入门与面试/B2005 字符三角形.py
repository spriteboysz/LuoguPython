#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:08
FileName: 入门与面试
Description:B2005 字符三角形.py 
"""


def func():
    ch = input().strip()
    chars = []
    for i in range(3):
        chars.append(str.center(ch * (i * 2 + 1), 5))
    print('\n'.join(chars))


if __name__ == '__main__':
    func()
