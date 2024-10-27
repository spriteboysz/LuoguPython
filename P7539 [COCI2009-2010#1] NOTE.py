#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 21:14
FileName: P7539 [COCI2009-2010#1] NOTE
Description:
"""


def func():
    nums = list(map(int, input().strip().split()))
    if nums == [1, 2, 3, 4, 5, 6, 7, 8]:
        print('ascending')
    elif nums == [8, 7, 6, 5, 4, 3, 2, 1]:
        print('descending')
    else:
        print('mixed')


if __name__ == '__main__':
    func()
