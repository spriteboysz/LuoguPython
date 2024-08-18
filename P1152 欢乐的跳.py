#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 14:52
FileName: 
Description:P1152 欢乐的跳.py 
"""


def func():
    data = list(map(int, input().strip().split()))
    n, *nums = data
    diff = [abs(nums[i] - nums[i - 1]) for i in range(1, n)]
    target = [i for i in range(1, n)]
    if set(target) == set(diff):
        print('Jolly')
    else:
        print('Not jolly')


if __name__ == '__main__':
    func()
