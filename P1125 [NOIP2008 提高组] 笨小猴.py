#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 18:30
FileName: 
Description:P1125 [NOIP2008 提高组] 笨小猴.py 
"""
from collections import defaultdict


def func():
    def check(num):
        if num == 0 or num == 1:
            return False
        elif num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    s = input().strip()
    cnt = defaultdict(int)
    for ch in s:
        cnt[ch] += 1
    maximum, minimum = max(cnt.values()), min(cnt.values())
    if check(maximum - minimum):
        print('Lucky Word')
        print(maximum - minimum)
    else:
        print('No Answer')
        print(0)


if __name__ == '__main__':
    func()
