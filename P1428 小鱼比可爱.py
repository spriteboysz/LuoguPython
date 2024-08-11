#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:32
FileName: 
Description:P1428 小鱼比可爱.py 
"""


def func():
    n = int(input().strip())
    nums1 = list(map(int, input().strip().split()))
    nums2 = [0]
    for i in range(1, n):
        curr = 0
        for j in range(0, i):
            if nums1[i] > nums1[j]:
                curr += 1
        nums2.append(curr)
    print(' '.join(map(str, nums2)))


if __name__ == '__main__':
    func()
