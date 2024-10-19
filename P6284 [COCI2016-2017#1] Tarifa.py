#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 17:40
FileName: 
Description:P6284 [COCI2016-2017#1] Tarifa.py 
"""


def func():
    x = int(input().strip())
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    print(n * x - sum(nums) + x)


if __name__ == '__main__':
    func()
