#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 09:08
FileName: 
Description:B3963 [语言月赛 202404] 吃苹果.py 
"""


def func():
    _ = input()
    nums = list(map(int, input().strip().split()))
    print(max(nums) + min(nums))


if __name__ == '__main__':
    func()
