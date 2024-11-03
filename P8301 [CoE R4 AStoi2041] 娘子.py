#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 09:41
FileName: Stoi2041] 娘子
Description:
"""


def func():
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    a1, b1 = a.count('1'), b.count('1')
    a0, b0 = n - a1, n - b1
    print(min(abs(a1 - b1), abs(a0 - b0)))


if __name__ == '__main__':
    func()
