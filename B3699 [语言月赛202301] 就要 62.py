#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-08 20:38
FileName: 
Description:B3699 [语言月赛202301] 就要 62.py 
"""


def func():
    x = int(input().strip())
    if '62' in str(x):
        print('Yes')
    elif x % 62 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
