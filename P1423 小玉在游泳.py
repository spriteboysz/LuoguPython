#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 10:38
FileName: 
Description:P1423 小玉在游泳.py 
"""


def func():
    s = float(input().strip())
    total, cur, cnt = 2, 2, 1
    while total < s:
        cur *= 0.98
        total += cur
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
