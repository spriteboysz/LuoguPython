#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:14
FileName: 
Description:B3824 [NICA #2] 台式烤香肠.py 
"""


def func():
    a, b, c = map(int, input().strip().split())
    d, e, f = map(int, input().strip().split())
    k = int(input())
    cnt1 = a * c * (k // b)
    cnt2 = d * f * (k // e)
    print(max(cnt1, cnt2))


if __name__ == '__main__':
    func()
