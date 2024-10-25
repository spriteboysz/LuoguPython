#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-25 20:54
FileName: P6488 [COCI2010-2011#6] OKUPLJANJE
Description:
"""


def func():
    l, p = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    print(' '.join([str(num - l * p) for num in nums]))


if __name__ == '__main__':
    func()
