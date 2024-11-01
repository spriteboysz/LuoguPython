#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-30 21:42
FileName: P7748 [COCI2013-2014#2] VOLIM
Description:
"""


def func():
    k = int(input().strip())
    n = int(input().strip())
    questions = [input().strip().split() for _ in range(n)]
    cur, acc = k - 1, 210
    for t, op in questions:
        if acc < int(t):
            print(cur + 1)
            return
        acc -= int(t)
        if op == 'T':
            cur += 1
            cur %= 8


if __name__ == '__main__':
    func()
