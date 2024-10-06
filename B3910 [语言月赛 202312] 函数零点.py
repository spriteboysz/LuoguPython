#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 19:20
FileName: 
Description:B3910 [语言月赛 202312] 函数零点.py 
"""


def func():
    _ = input()
    nums = list(map(int, input().strip().split()))
    cnt = 0
    for i, num in enumerate(nums[1:], 1):
        if nums[i - 1] * num < 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
