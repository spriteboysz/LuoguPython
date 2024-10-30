#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-29 23:06
FileName: P7625 [COCI2011-2012#1] JABUKE
Description:
"""


def func():
    n, m = map(int, input().strip().split())
    t = int(input().strip())
    nums = [int(input().strip()) for _ in range(t)]
    left = 1
    cnt = 0
    for num in nums:
        if num < left:
            cnt += left - num
            left = num
        else:
            right = left + m - 1
            if num > right:
                cnt += num - right
                right = num
                left = right + 1 - m
    print(cnt)


if __name__ == '__main__':
    func()
