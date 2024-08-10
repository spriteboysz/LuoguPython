#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:49
FileName: 
Description:P5719 【深基4.例3】分类平均.py 
"""


def func():
    n, k = map(int, input().strip().split())
    nums1, nums2 = [], []
    for num in range(1, n + 1):
        if num % k == 0:
            nums1.append(num)
        else:
            nums2.append(num)
    print(f'{sum(nums1) / len(nums1):.1f} {sum(nums2) / len(nums2):.1f}')


if __name__ == '__main__':
    func()
