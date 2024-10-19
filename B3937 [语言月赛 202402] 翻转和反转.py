#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 10:17
FileName: 
Description:B3937 [语言月赛 202402] 翻转和反转.py 
"""


def func():
    _, _ = map(int, input().strip().split())
    s = input().strip()
    w = input().strip()
    cnt1, cnt2 = w.count('1'), w.count('2')
    if cnt2 % 2 == 1:
        s = ''.join([str(1 - int(c)) for c in s])
    if cnt1 % 2 == 1:
        s = s[::-1]
    print(s)


if __name__ == '__main__':
    func()
