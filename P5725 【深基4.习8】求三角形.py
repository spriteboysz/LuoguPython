#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 11:38
FileName: 
Description:P5725 【深基4.习8】求三角形.py 
"""


def func():
    n = int(input().strip())

    cnt = 0
    for i in range(1, n * n + 1):
        cnt += 1
        print(f'{i:02d}', end='')
        if cnt == n:
            print()
            cnt = 0

    cnt, cur = 0, 0
    for i in range(1, ((1 + n) * n // 2) + 1):
        if cnt == cur:
            cur += 1
            cnt = 0
            print()
            print(' ' * (n - cur) * 2, end='')
        cnt += 1
        print(f'{i:02d}', end='')


if __name__ == '__main__':
    func()
