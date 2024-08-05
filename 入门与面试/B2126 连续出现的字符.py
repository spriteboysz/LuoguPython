#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 22:54
FileName: 入门与面试
Description:B2126 连续出现的字符.py 
"""


def func():
    k = int(input().strip())
    s = input().strip()
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= k:
            print(s[i])
            return
    print('No')


if __name__ == '__main__':
    func()
