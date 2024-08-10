#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:22
FileName: 入门与面试
Description:B2118 验证子串.py 
"""


def func():
    s1, s2 = input().strip(), input().strip()
    if s1 in s2:
        print(f'{s1} is substring of {s2}')
    elif s2 in s1:
        print(f'{s2} is substring of {s1}')
    else:
        print('No substring')


if __name__ == '__main__':
    func()
