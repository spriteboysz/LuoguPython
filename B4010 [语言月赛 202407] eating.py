#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-24 22:36
FileName: 
Description:B4010 [语言月赛 202407] eating.py 
"""


def func():
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    maximum = max(data, key=lambda el: (el[1] / el[0], -el[0]))
    print(maximum[0])


if __name__ == '__main__':
    func()
