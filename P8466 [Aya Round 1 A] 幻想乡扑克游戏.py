#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 21:29
FileName: P8466 [Aya Round 1 A] 幻想乡扑克游戏
Description:
"""
from collections import Counter


def func():
    t = int(input().strip())
    data = [input().strip() for _ in range(t)]
    for row in data:
        if max(Counter(row).values()) == 4 or ('D' in row and 'X' in row):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    func()
