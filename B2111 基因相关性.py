#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:43
FileName: 入门与面试
Description:B2111 基因相关性.py 
"""


def func():
    v = float(input().strip())
    s1, s2 = input().strip(), input().strip()
    cnt = 0
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            cnt += 1
    print('yes' if cnt / len(s1) >= v else 'no')


if __name__ == '__main__':
    func()
