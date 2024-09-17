#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:59
FileName: 
Description:B3864 [GESP202309 一级] 小明的幸运数.py 
"""


def func():
    k, l, r = [int(input().strip()) for _ in range(3)]
    cnt = 0
    for num in range(l, r + 1):
        if num % k == 0 or num % 10 == k:
            cnt += num
    print(cnt)


if __name__ == '__main__':
    func()
