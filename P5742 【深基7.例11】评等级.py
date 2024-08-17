#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 09:50
FileName: 
Description:P5742 【深基7.例11】评等级.py 
"""


def func():
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    for _, a, b in data:
        if a + b > 140 and a * 7 + b * 3 >= 800:
            print('Excellent')
        else:
            print('Not excellent')


if __name__ == '__main__':
    func()
