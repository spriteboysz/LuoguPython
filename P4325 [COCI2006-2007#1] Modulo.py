#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 09:56
FileName: 
Description:P4325 [COCI2006-2007#1] Modulo.py 
"""


def func():
    nums = [int(input().strip()) % 42 for _ in range(10)]
    print(len(set(nums)))


if __name__ == '__main__':
    func()
