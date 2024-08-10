#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 09:54
FileName: 入门与面试
Description:B3633 集合运算 2.py 
"""


def func():
    _ = int(input().strip())
    nums1 = set(map(int, input().strip().split()))
    _ = int(input().strip())
    nums2 = set(map(int, input().strip().split()))
    nums3 = set([i for i in range(0, 64)])

    print(len(nums1))
    print(' '.join(map(str, sorted(list(nums1 & nums2)))))
    print(' '.join(map(str, sorted(list(nums1 | nums2)))))
    print(' '.join(map(str, sorted(list(nums3 - nums1)))))
    print(int(nums1 == nums2))
    print(int(nums1 & nums2 == nums1))
    print(int(0 in nums1))


if __name__ == '__main__':
    func()
