#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 19:47
FileName: 
Description:B3907 [语言月赛 202312] NK.py 
"""


def func():
    n, k = map(int, input().strip().split())
    cnt = 0
    for i in range(n, n ** n + 1, 10):
        if i % k % n == 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
