#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 19:58
FileName: 
Description:B3795 [NICA #1] 成绩.py 
"""


def func():
    a, b, c, d, e, f = map(int, input().strip().split())
    s1 = sum(map(lambda el: el // 60, [a, b, c])) >= 2
    s2 = (a * d + b * e + c * f) / (d + e + f) >= 60
    print('PASS' if s1 else 'FAIL')
    print('PASS' if s2 else 'FAIL')


if __name__ == '__main__':
    func()
