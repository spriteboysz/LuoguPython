#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 22:06
FileName: P6850 NOI
Description:
"""

def func():
    a, *nums, h, i = map(int, input().strip().split())
    score = 50 + a + sum(nums)
    if h == 1:
        score += 5
    if score >= i:
        print('AKIOI')
    else:
        print('AFO')

if __name__ == '__main__':
    func()
