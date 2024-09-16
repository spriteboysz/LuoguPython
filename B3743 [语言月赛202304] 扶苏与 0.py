#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:33
FileName: 
Description:B3743 [语言月赛202304] 扶苏与 0.py 
"""


def func():
    num = input().strip()
    digits = [1, 0, 1, 0, 0, 0, 1, 0, 2, 1]
    print(sum([digits[int(c)] for c in num]))


if __name__ == '__main__':
    func()
