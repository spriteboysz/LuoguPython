#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 22:46
FileName: P9950 [USACO20FEB] Mad Scientist B
Description:
"""


def func():
    _ = input()
    s1 = input().strip()
    s2 = input().strip()
    diff = []
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            diff.append(' ')
        else:
            diff.append('D')
    print(len(''.join(diff).split()))


if __name__ == '__main__':
    func()
