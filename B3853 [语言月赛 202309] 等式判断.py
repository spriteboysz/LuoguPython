#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 11:42
FileName: 
Description:B3853 [语言月赛 202309] 等式判断.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    if a + b == c:
        print('plus')
    elif a - b == c:
        print('minus')
    else:
        print('illegal')


if __name__ == '__main__':
    func()
