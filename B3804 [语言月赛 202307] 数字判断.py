#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 20:25
FileName: 
Description:B3804 [语言月赛 202307] 数字判断.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    flag1, flag2, flag3, flag4 = [False] * 4
    if a + b + c <= 100:
        flag1 = True
    if b % 5 == 0:
        flag2 = True
    if c % 7 == 0:
        flag3 = True
    if a - b > b - c:
        flag4 = True
    if flag1 and flag2 and flag3 and flag4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
