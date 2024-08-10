#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 19:04
FileName: 
Description:P5721 【深基4.例6】数字直角三角形.py 
"""


def func():
    n = int(input().strip())
    k, cnt = n, 0
    for num in range(1, (n * (n + 1) // 2) + 1):
        print(f'{num:02d}', end='')
        cnt += 1
        if cnt == k:
            k -= 1
            cnt = 0
            print()


if __name__ == '__main__':
    func()
