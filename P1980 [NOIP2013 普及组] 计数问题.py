#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 20:03
FileName: 
Description:P1980 [NOIP2013 普及组] 计数问题.py 
"""


def func():
    n, x = input().strip().split()
    print(sum([list(str(i + 1)).count(x) for i in range(int(n))]))


if __name__ == '__main__':
    func()
