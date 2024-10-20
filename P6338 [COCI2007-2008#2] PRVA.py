#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-20 08:36
FileName: 
Description:P6338 [COCI2007-2008#2] PRVA.py 
"""


def func():
    r, c = map(int, input().strip().split())
    grid = [input().strip() for _ in range(r)]
    words = []
    for row in grid:
        words.extend(row.split('#'))
    for row in zip(*[list(row) for row in grid]):
        words.extend(''.join(row).split('#'))
    words = [word for word in words if len(word) >= 2]
    words.sort()
    print(words[0])

if __name__ == '__main__':
    func()
