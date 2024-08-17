#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 10:47
FileName: 
Description:P1042 [NOIP2003 普及组] 乒乓球.py 
"""

import sys


def func():
    def process(mode):
        a, b = 0, 0
        for ch in data:
            if ch == 'W':
                a += 1
            else:
                b += 1
            if max(a, b) >= mode and abs(a - b) >= 2:
                print(f'{a}:{b}')
                a, b = 0, 0
        print(f'{a}:{b}')

    data = ''
    while True:
        try:
            data += sys.stdin.readline().strip()
        except EOFError:
            break
        if 'E' in data:
            break
    data = data.split('E')[0]
    process(11)
    print()
    process(21)


if __name__ == '__main__':
    func()
