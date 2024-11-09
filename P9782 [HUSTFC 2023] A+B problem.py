#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 22:30
FileName: P9782 [HUSTFC 2023] A+B problem
Description:
"""
from string import ascii_uppercase as uppercase


def func():
    s, t = input().strip().split()
    a = uppercase.index(s) + uppercase.index(t)
    if a < 26:
        print(uppercase[a])
    else:
        div, mod = divmod(a, 26)
        print(f'{uppercase[div]}{uppercase[mod]}')


if __name__ == '__main__':
    func()
