#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 21:58
FileName: 
Description:B3652 [语言月赛202208] 渡荆门送别.py 
"""
import itertools


def func():
    _ = input()
    nums = map(int, input().strip().split())
    nums1, nums2, nums3, nums4 = itertools.tee(nums, 4)
    maximum, minimum = max(nums1), min(nums2)
    print(' '.join(map(lambda el: str(maximum - el), nums3)))
    print(' '.join(map(lambda el: str(el - minimum), nums4)))


if __name__ == '__main__':
    func()
