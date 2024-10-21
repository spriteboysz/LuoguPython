#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024/10/20 23:35
FileName: B3684 [语言月赛202212] 不可以，总司令
Description:
"""

def func():
    a, b = map(int, input().strip().split())
    if a > b:
        print('no')
    elif a < b:
        print('yes')
    else:
        print('equal probability')

if __name__ == '__main__':
    func()