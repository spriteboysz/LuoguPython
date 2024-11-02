#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 11:04
FileName: P7772 [COCI2009-2010#2] FAKTOR
Description:
"""


def func():
    a, i = map(int, input().strip().split())
    print(a * (i - 1) + 1)


if __name__ == '__main__':
    func()
