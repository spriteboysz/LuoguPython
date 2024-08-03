#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:50
FileName: 入门与面试
Description:B2088 计算书费.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    prices = [28.9, 32.7, 45.6, 78, 35, 86.2, 27.8, 43, 56, 65]
    total = sum([num * price for num, price in zip(nums, prices)])
    print(f'{total:.1f}')


if __name__ == '__main__':
    func()
