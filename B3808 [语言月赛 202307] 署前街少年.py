#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 21:12
FileName: 
Description:B3808 [语言月赛 202307] 署前街少年.py 
"""


def func():
    n, k = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    quadrant = [0] * k
    for i, num in enumerate(nums):
        quadrant[i % k] += num

    for i in range(0, n * 2, 2):
        nums[i] = quadrant[i % k] % (i+1)
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    func()
