#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 10:44
FileName: 
Description:B3973 [语言月赛 202405] 小 S 大战小 Q.py 
"""


def func():
    _ = input()
    nums1 = list(map(int, input().strip().split()))
    nums2 = list(map(int, input().strip().split()))
    s, q = 0, 0
    for num1, num2 in zip(nums1, nums2):
        if num1 > num2:
            s += 1
        elif num1 < num2:
            q += 1
    print(s, q)
    if s == q:
        print('Tie')
    else:
        print('S' if s > q else 'Q')


if __name__ == '__main__':
    func()
