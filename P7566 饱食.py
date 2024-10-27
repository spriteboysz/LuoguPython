#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 22:44
FileName: P7566 饱食
Description:
"""

def func():
    n = int(input().strip())
    words = [input().strip()[0] for _ in range(n)]
    a, b, c, d = words.count('M'), words.count('C'), words.count('O'), words.count('I')
    cnt = a * b * c + a * b * d + a * c * d + b * c * d
    print(cnt)

if __name__ == '__main__':
    func()
