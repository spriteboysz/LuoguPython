#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 21:40
FileName: 
Description:P2669 [NOIP2015 普及组] 金币.py 
"""


def func():
    k = int(input().strip())
    golds, curr = [], 1
    cnt = 0
    for i in range(1, k + 1):
        cnt += 1
        golds.append(curr)
        if cnt >= curr:
            curr += 1
            cnt = 0
    print(sum(golds))


if __name__ == '__main__':
    func()
