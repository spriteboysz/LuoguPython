#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:54
FileName: 
Description:B4019 [语言月赛 202408] 皆与生物有缘.py 
"""
import math


def func():
    _ = input()
    nums1 = sum(map(int, input().strip().split()))
    nums2 = sum(map(int, input().strip().split()))
    print(math.ceil((nums1 + nums2) / 2))


if __name__ == '__main__':
    func()
