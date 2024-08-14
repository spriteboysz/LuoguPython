#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 22:32
FileName: 
Description:P1553 数字反转（升级版）.py 
"""


def func():
    s = input().strip()
    if s.endswith('%'):
        print(f'{int(s[:-1][::-1])}%')
    elif '/' in s:
        a, b = s.split('/')
        print(f'{int(a[::-1])}/{int(b[::-1])}')
    elif '.' in s:
        a, b = s.split('.')
        print(f'{int(a[::-1])}.{str(int(b))[::-1]}')
    else:
        print(f'{int(s[::-1])}')


if __name__ == '__main__':
    func()
