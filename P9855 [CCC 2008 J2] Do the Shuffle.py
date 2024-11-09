#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 22:07
FileName: P9855 [CCC 2008 J2] Do the Shuffle
Description:
"""


def func():
    data = ['A', 'B', 'C', 'D', 'E']
    while True:
        b = int(input().strip())
        n = int(input().strip()) % 5
        if b == 1:
            data = data[n:] + data[:n]
        if b == 2:
            data = data[-n:] + data[:-n]
        if b == 3 and n % 2 == 1:
            data[0], data[1] = data[1], data[0]
        if b == 4:
            print(' '.join(data))
            break


if __name__ == '__main__':
    func()
