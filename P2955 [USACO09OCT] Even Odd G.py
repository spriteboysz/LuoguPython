#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-22 23:15
FileName: 
Description:P2955 [USACO09OCT] Even Odd G.py 
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    for num in nums:
        if num % 2 == 0:
            print('even')
        else:
            print('odd')


if __name__ == '__main__':
    func()
