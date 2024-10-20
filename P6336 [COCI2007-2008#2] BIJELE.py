#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 20:26
FileName: 
Description:P6336 [COCI2007-2008#2] BIJELE.py 
"""


def func():
    nums1 = map(int, input().strip().split())
    nums2 = [1, 1, 2, 2, 2, 8]
    print(' '.join(map(str, [num2 - num1 for num1, num2 in zip(nums1, nums2)])))


if __name__ == '__main__':
    func()
