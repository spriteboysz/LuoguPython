#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:48
FileName: 
Description:B3956 [GESP202403 三级] 字母求和.py 
"""
from string import ascii_lowercase, ascii_uppercase


def func():
    dic1 = {c: i + 1 for i, c in enumerate(ascii_lowercase)}
    dic2 = {c: -ord(c) for c in ascii_uppercase}
    dic1.update(dic2)
    _ = input()
    s = input().strip()
    print(sum([dic1.get(c) for c in s]))


if __name__ == '__main__':
    func()
