#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 22:11
FileName: P7540 [COCI2009-2010#1] DOMINO
Description:
"""


def func():
    n = int(input().strip())
    sum1, sum2 = 0, 0
    acc = sum([i for i in range(n + 1)])
    for i in range(n + 1):
        sum1 += (n - i + 1) * i
        sum2 += acc
        acc -= i
    print(sum1 + sum2)


if __name__ == '__main__':
    func()
