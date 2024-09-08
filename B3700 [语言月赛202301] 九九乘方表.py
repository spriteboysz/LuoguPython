#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-08 20:40
FileName: 
Description:B3700 [语言月赛202301] 九九乘方表.py 
"""


def func():
    n = int(input().strip())
    for i in range(1, n + 1):
        for j in range(1, i +1):
            print(f'{i} ^ {j} = {i**j}', end=' ')
        print()


if __name__ == '__main__':
    func()
