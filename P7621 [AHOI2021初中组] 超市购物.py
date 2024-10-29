#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-28 23:21
FileName: P7621 [AHOI2021初中组] 超市购物
Description:
"""


def func():
    n = int(input().strip())
    total = 0.0

    for _ in range(n):
        a, b = map(float, input().split())
        total += a * b

    print(f'{total * 0.85 - 0.049:.1f}')



if __name__ == '__main__':
    func()
