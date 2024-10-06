#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:30
FileName: 
Description:P8833 [传智杯 #3 决赛] 课程.py 
"""


def func():
    _ = input()
    nums1 = map(int, input().strip().split())
    nums2 = map(int, input().strip().split())
    print(len(set(nums1) & set(nums2)))


if __name__ == '__main__':
    func()
