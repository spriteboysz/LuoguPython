#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-23 22:29
FileName: 
Description:P4439 [COCI2017-2018#3] Aron.py 
"""


def func():
    n = int(input().strip())
    colors = [input().strip() for _ in range(n)]
    stack = []
    for color in colors:
        if not stack:
            stack.append(color)
        elif color != stack[-1]:
            stack.append(color)

    print(len(stack) + 1)


if __name__ == '__main__':
    func()
