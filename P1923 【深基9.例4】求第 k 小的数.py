#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 15:00
FileName: 
Description:P1923 【深基9.例4】求第 k 小的数.py 
"""


def func():
    _, k = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    print(sorted(nums)[k])


if __name__ == '__main__':
    func()
