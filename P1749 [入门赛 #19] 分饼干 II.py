#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:54
FileName: 
Description:P1749 [入门赛 #19] 分饼干 II.py 
"""


def func():
    t = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(t)]
    for n, k in data:
        if (1 + k) * k // 2 > n:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    func()
