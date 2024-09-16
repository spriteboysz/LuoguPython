#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 14:49
FileName: 
Description:B3763 [语言月赛202305] 团体程序设计天梯赛.py 
"""


def func():
    nums1 = sum(map(int, input().strip().split()))
    nums2 = sum(map(int, input().strip().split()))
    nums3 = sum(map(int, input().strip().split()))
    if nums1 < 80:
        print(nums1)
    elif nums2 < 40:
        print(nums1 + nums2)
    else:
        print(nums1 + nums2 + nums3)


if __name__ == '__main__':
    func()
