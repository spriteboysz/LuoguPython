#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:32
FileName: 
Description:P8834 [传智杯 #3 决赛] 序列.py 
"""


def func():
    n, k = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    cnt = 0
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[:i]):
            if num1 * num2 <= k:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
