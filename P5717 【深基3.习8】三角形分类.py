#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:58
FileName: 
Description:P5717 【深基3.习8】三角形分类.py 
"""


def func():
    a, b, c = sorted(map(int, input().strip().split()))
    if a + b <= c:
        print('Not triangle')
        return
    if a * a + b * b == c * c:
        print('Right triangle')
    if a * a + b * b > c * c:
        print('Acute triangle')
    if a * a + b * b < c * c:
        print('Obtuse triangle')
    if len({a, b, c}) <= 2:
        print('Isosceles triangle')
    if len({a, b, c}) == 1:
        print('Equilateral triangle')


if __name__ == '__main__':
    func()
