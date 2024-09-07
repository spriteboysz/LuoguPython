#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 22:11
FileName: 
Description:B3651 [语言月赛202208] 数组调整.py 
"""
import itertools


def func():
    n, k = map(int, input().strip().split())
    nums = map(int, input().strip().split())
    nums1, nums2 = itertools.tee(nums, 2)
    for i, num in enumerate(nums1):
        if i == k - 1:
            print(sum(nums2) - 2 * num)
            return


if __name__ == '__main__':
    func()
