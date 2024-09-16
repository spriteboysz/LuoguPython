#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:54
FileName: 
Description:B3844 [GESP样题 二级] 画正方形.py 
"""

from string import ascii_uppercase


def func():
    n = int(input().strip())
    chars = ascii_uppercase * 4
    for i in range(n):
        print(chars[i:i + n])


if __name__ == '__main__':
    func()
