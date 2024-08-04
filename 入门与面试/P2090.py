#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 09:20
FileName: 入门与面试
Description:P2090.py 
"""


def func():
    n = int(input().strip())
    ages = list(map(int, input().strip().split()))
    count = [0] * 4
    for age in ages:
        if 0 <= age <= 18:
            count[0] += 1
        elif 19 <= age <= 35:
            count[1] += 1
        elif 36 <= age <= 60:
            count[2] += 1
        else:
            count[3] += 1
    print('\n'.join(map(lambda cnt: f'{cnt * 100 / n:.2f}%', count)))


if __name__ == '__main__':
    func()
