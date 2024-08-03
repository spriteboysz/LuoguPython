#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:50
FileName: 入门与面试
Description:B2053 求一元二次方程.py 
"""


def func():
    a, b, c = map(float, input().strip().split())
    temp = b * b - 4 * a * c
    if temp < 0:
        print('No answer!')
    elif temp == 0:
        print(f'x1=x2={-b / (2 * a):.5f}')
    else:
        x1 = (- b - temp ** 0.5) / (2 * a)
        x2 = (- b + temp ** 0.5) / (2 * a)
        x1, x2 = sorted([x1, x2])
        print(f'x1={x1:.5f};x2={x2:.5f}')


if __name__ == '__main__':
    func()
