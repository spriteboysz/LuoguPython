#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 16:20
FileName: 
Description:P2911 [USACO08OCT] Bovine Bones G.py 
"""
from collections import defaultdict


def func():
    s1, s2, s3 = map(int, input().strip().split())
    cnt = defaultdict(int)
    for num1 in range(1, s1 + 1):
        for num2 in range(1, s2 + 1):
            for num3 in range(1, s3 + 1):
                cnt[num1 + num2 + num3] += 1
    maximum = max(cnt.values())
    for i in range(s1 + s2 + s3 + 1):
        if cnt[i] == maximum:
            print(i)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
