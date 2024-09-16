#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:51
FileName: 
Description:B3839 [GESP202306 一级] 累计相加.py 
"""


def func():
    n = int(input().strip())
    acc, total = 0, 0
    for i in range(1, n + 1):
        total += i
        acc += total
    print(acc)


if __name__ == '__main__':
    func()
