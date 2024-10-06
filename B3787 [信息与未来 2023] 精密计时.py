#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:56
FileName: 
Description:B3787 [信息与未来 2023] 精密计时.py 
"""


def func():
    def process(t):
        t = t.replace('.', ':')
        hh, mm, ss, ms = map(int, t.split(':'))
        return (hh * 3600 + mm * 60 + ss) * 100 + ms

    start, end = input().strip().split()
    print(process(end) - process(start))


if __name__ == '__main__':
    func()
