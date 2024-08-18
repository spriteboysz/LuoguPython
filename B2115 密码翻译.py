#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 11:48
FileName: 
Description:B2115 密码翻译.py 
"""


def func():
    s = input().strip()
    ss = ''
    for ch in s:
        if 'b' <= ch <= 'z' or 'B' <= ch <= 'Z':
            ss += chr(ord(ch) - 1)
        elif ch == 'a':
            ss += 'z'
        elif ch == 'A':
            ss += 'Z'
        else:
            ss += ch
    print(ss)


if __name__ == '__main__':
    func()
