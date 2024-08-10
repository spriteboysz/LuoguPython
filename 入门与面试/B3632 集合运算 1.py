#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 09:40
FileName: 入门与面试
Description:B3632 集合运算 1.py 
"""


def func():
    _ = int(input().strip())
    nums1 = list(map(int, input().strip().split()))
    _ = int(input().strip())
    nums2 = list(map(int, input().strip().split()))
    print(len(set(nums1)))
    print(' '.join(map(str, sorted(list(set(nums1) & set(nums2))))))
    print(' '.join(map(str, sorted(list(set(nums1) | set(nums2))))))


if __name__ == '__main__':
    func()
