#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:25
FileName: 
Description:P1046 [NOIP2005 普及组] 陶陶摘苹果.py 
"""


def func():
    highs = list(map(int, input().strip().split()))
    maximum = int(input().strip()) + 30
    print(sum([int(maximum >= high) for high in highs]))


if __name__ == '__main__':
    func()
