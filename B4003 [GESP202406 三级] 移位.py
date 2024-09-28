#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:36
FileName: 
Description:B4003 [GESP202406 三级] 移位.py 
"""
from string import ascii_uppercase


def func():
    n = int(input().strip()) % 26
    uppercase = ascii_uppercase * 2
    print(uppercase[n:n + 26])


if __name__ == '__main__':
    func()
