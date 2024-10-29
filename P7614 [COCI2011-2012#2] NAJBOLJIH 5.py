#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-28 22:50
FileName: P7614 [COCI2011-2012#2] NAJBOLJIH 5
Description:
"""


def func():
    nums = [(int(input().strip()), i + 1) for i in range(8)]
    nums.sort(key=lambda el: -el[0])
    print(sum(map(lambda el: el[0], nums[:5])))
    print(' '.join(map(str, sorted(map(lambda el: el[1], nums[:5])))))


if __name__ == '__main__':
    func()
