#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 22:22
FileName: P6723 [COCI2015-2016#5] ZAMKA
Description:
"""

def func():
    l = int(input().strip())
    d = int(input().strip())
    x = int(input().strip())
    for i in range(l, d + 1):
        if sum(map(int, list(str(i)))) == x:
            print(i)
            break
    for i in range(d, l - 1, -1):
        if sum(map(int, list(str(i)))) == x:
            print(i)
            break

if __name__ == '__main__':
    func()
