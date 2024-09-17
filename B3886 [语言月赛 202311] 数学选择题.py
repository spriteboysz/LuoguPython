#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 18:40
FileName: 
Description:B3886 [语言月赛 202311] 数学选择题.py 
"""


def func():
    a, b, c, d, m = map(int, input().strip().split())
    if c * 5 <= m:
        print(max(0, (c * 5 - (b - d) * 20)))
    else:
        print(max(0, (c * 5 + d * 20 - (b - d) * 20)))


if __name__ == '__main__':
    func()
