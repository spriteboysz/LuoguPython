#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 09:28
FileName: P7797 [COCI2015-2016#6] BELA
Description:
"""


def func():
    data = {
        'A': [11, 11],
        'K': [4, 4],
        'Q': [3, 3],
        'J': [20, 2],
        'T': [10, 10],
        '9': [14, 0],
        '8': [0, 0],
        '7': [0, 0]
    }

    n, b = input().strip().split()
    nums = [input().strip() for _ in range(4 * int(n))]
    total = 0
    for num in nums:
        if num[-1] == b:
            total += data[num[0]][0]
        else:
            total += data[num[0]][1]
    print(total)


if __name__ == '__main__':
    func()
