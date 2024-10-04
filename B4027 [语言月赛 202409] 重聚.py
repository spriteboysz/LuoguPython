#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 09:42
FileName: 
Description:B4027 [语言月赛 202409] 重聚.py 
"""


def func():
    t, d, t1, d1, t2, d2 = map(int, input().strip().split())
    t10, t20 = -1, -1
    if d <= d1:
        t10 = max(0, t1 - t)
    if d <= d2:
        t20 = max(0, t2 - t)
    if t10 == -1 and t20 == -1:
        print(-1)
    elif t10 == -1:
        print(t20)
    elif t20 == -1:
        print(t10)
    else:
        print(min(t10, t20))


if __name__ == '__main__':
    func()
