#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:45
FileName: 
Description:P8841 [传智杯 #4 初赛] 竞争得分.py 
"""


def func():
    _ = input()
    nums = list(map(int, input().strip().split()))
    maximum, minimum = max(nums), min(nums)
    print(' '.join(map(str, [(num - minimum) * 100 // (maximum - minimum) for num in nums])))


if __name__ == '__main__':
    func()
