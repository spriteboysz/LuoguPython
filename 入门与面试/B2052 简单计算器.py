#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:45
FileName: 入门与面试
Description:B2052 简单计算器.py 
"""


def func():
    a, b, op = input().strip().split()
    a, b = map(int, [a, b])
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b == 0:
            print('Divided by zero!')
        else:
            print(a // b)
    else:
        print('Invalid operator!')


if __name__ == '__main__':
    func()
